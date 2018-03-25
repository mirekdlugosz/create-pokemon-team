import { environment } from '../../environments/environment';
import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

import { Subject, BehaviorSubject } from 'rxjs';

import { MovesService } from './moves.service';

@Injectable()
export class PokemonService {
  private _version: string;
  private _transferred: boolean;
  private _pokedex: any[];
  private _pokemonLearnsets: {};
  private _requestedPokemon: any[] = [];

  // I find the fact that I have to set these up ridiculous
  private _versionSet$ = new Subject();
  private _learnsetsSet$ = new Subject();

  // we must use BehaviorSubject here, as some components are consuming it
  public availablePokemon$ = new BehaviorSubject<any[]>([]);
  public pokemonDetails$ = new BehaviorSubject({});
  public requestedMoves$ = new Subject();

  constructor(private http: HttpClient, private ms: MovesService) {
    this._versionSet$.subscribe(d => this.obtainLearnsets());
    this._learnsetsSet$.subscribe(d => this.obtainMovesData());
  }

  public stateChangedHandler(data) {
    this._requestedPokemon = data.requestedPokemon;
    this.versionHandler(data.versionInfo);
  }

  private versionHandler(data) {
    const newTransferred = data.transferred;
    if (newTransferred !== this._transferred) {
      this._transferred = newTransferred;
      this._pokemonLearnsets = {};
    }

    const newVersion = data.version;
    if (newVersion !== this._version) {
      this._version = newVersion;
      this._pokemonLearnsets = {};

      const url = `${environment.endpoint}pokemon`;
      const options = {params: new HttpParams().set('ver', this._version)};

      this.http
        .get<any[]>(url, options)
        .subscribe(result => {
          this._pokedex = result;
          this._requestedPokemon = this._requestedPokemon
            .filter(pokemon => this._pokedex.map(p => p.id).includes(pokemon));
          const availablePokemon = this._pokedex
            .map(pokemonObj => ({'id': pokemonObj.id, 'name': pokemonObj.name}));
          this.availablePokemon$.next(availablePokemon);
          this._versionSet$.next(true);
        });
    } else {
      this._versionSet$.next(true);
    }
  }

  private obtainLearnsets() {
    // none of requested pokemon exist in this generation
    if (this._requestedPokemon.length === 0) {
      this.pokemonDetails$.next({});
      return;
    }

    const missingFromLearnsets = this._requestedPokemon
      .filter((pokemon, num, arr) => arr.indexOf(pokemon) === num)
      .filter(pokemon => !(pokemon in this._pokemonLearnsets));

    if (missingFromLearnsets.length > 0) {
      const url = `${environment.endpoint}pokemon`;
      let params = new HttpParams().set('ver', this._version);
      if (this._transferred === true) {
        params = params.set('transferred', 'true');
      }
      for (const pokemon of missingFromLearnsets) {
        params = params.append('p', pokemon);
      }

      this.http
        .get<any[]>(url, {'params': params})
        .subscribe(result => {
          Object.assign(this._pokemonLearnsets, result);
          this._learnsetsSet$.next(true);
        });
    } else {
      this._learnsetsSet$.next(true);
    }
  }

  private obtainMovesData() {
    // Single array of all moves that requested Pokemon can learn
    const moves = [].concat(
      ...this._requestedPokemon.map(name => this._pokemonLearnsets[name])
    ).filter(name => name !== undefined)
      .filter((name, num, arr) => arr.indexOf(name) === num);

    if (moves.length === 0) {
      return;
    }

    this.requestedMoves$.next({'version': this._version, 'moves': moves});
  }

  public movesDataHandler(data) {
    const struct = {};
    this._requestedPokemon
      .filter(pokemon => this._pokemonLearnsets[pokemon] !== undefined)
      .forEach(pokemon => {
      const pokemonObj = Object.assign({}, this._pokedex.find(p => p.id === pokemon));
      const moves = this._pokemonLearnsets[pokemon].map(move => {
        const type = data[move]['uses_pokemon_type'] ? {'type': pokemonObj['type'][0]} : {};
        return Object.assign({}, data[move], {'id': move}, type);
      });
      struct[pokemon] = {'pokemon': pokemonObj, 'moves': moves};
    });
    this.pokemonDetails$.next(struct);
  }
}
