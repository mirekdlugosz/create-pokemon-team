import { Subject, combineLatest } from 'rxjs';
import { filter, withLatestFrom, debounceTime, takeUntil } from 'rxjs/operators';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';

import { UrlmanagerService } from '../../services/urlmanager.service';
import { TeamService } from '../../services/team.service';
import { PokemonService } from '../../services/pokemon.service';
import { MovesService } from '../../services/moves.service';
import { TypeEffectivenessService } from '../../services/typeeffectiveness.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html'
})
export class IndexComponent implements OnInit, OnDestroy {
  private _componentDestroyed$ = new Subject();

  constructor(
    private route: ActivatedRoute,
    private urlmanagerService: UrlmanagerService,
    private teamService: TeamService,
    private pokemonService: PokemonService,
    private movesService: MovesService,
    private typeEffectivenessService: TypeEffectivenessService
  ) { }

  ngOnInit() {
    this.route.queryParamMap.pipe(
      debounceTime(10), // I hate this idea, but see https://github.com/angular/angular/issues/12157
      takeUntil(this._componentDestroyed$)
    ).subscribe(params => this.urlmanagerService.paramsChanged(params));
    this.urlmanagerService.teamDefinition$
      .pipe(takeUntil(this._componentDestroyed$))
      .subscribe(d => this.teamService.createTeamFromURL(d));
    this.teamService.teamDataRequest$.pipe(
      withLatestFrom(
        this.urlmanagerService.version$,
        (pokemonData, version) => ({'versionInfo': version, 'requestedPokemon': pokemonData})
      ),
      takeUntil(this._componentDestroyed$)
    ).subscribe(d => this.pokemonService.stateChangedHandler(d));
    this.pokemonService.requestedMoves$
      .pipe(takeUntil(this._componentDestroyed$))
      .subscribe(d => this.movesService.movesRequestHandler(d));
    this.movesService.movesData$
      .pipe(takeUntil(this._componentDestroyed$))
      .subscribe(d => this.pokemonService.movesDataHandler(d));
    this.pokemonService.pokemonDetails$
      .pipe(takeUntil(this._componentDestroyed$))
      .subscribe(d => this.teamService.fillTeamData(d));
    this.urlmanagerService.version$
      .pipe(takeUntil(this._componentDestroyed$))
      .subscribe(d => this.typeEffectivenessService.versionSet(d));
  }

  ngOnDestroy() {
    this._componentDestroyed$.next(true);
    this._componentDestroyed$.complete();
  }

}
