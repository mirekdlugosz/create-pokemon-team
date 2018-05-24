/**
 * createPokémon.team - web application that helps you build your own
 * Pokémon team in any core series game
 * Copyright © 2018  Mirosław Zalewski
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * any later version.
 */

import { Component, OnInit, OnChanges, Input, Output, EventEmitter } from '@angular/core';
import { PokemonService } from '../../services/pokemon.service';

@Component({
  selector: 'app-pokemon-selector',
  templateUrl: './pokemon-selector.component.html',
  styleUrls: ['./pokemon-selector.component.scss']
})
export class PokemonSelectorComponent implements OnInit, OnChanges {
  public pokemonList: any[];
  private pokemonMovesList: any[];
  private pokemonId = '';

  @Input()
  label: string;

  @Input()
  pokemon;

  @Input()
  position?: number;

  @Output()
  pokemonChanged = new EventEmitter();

  constructor(private pokemonService: PokemonService) { }

  ngOnInit() {
    this.pokemonService.availablePokemon$.subscribe(d => this.pokemonList = d);
  }

  ngOnChanges(changes) {
    if (!('pokemon' in changes) || changes.pokemon.currentValue === undefined) {
      return;
    }
    this.pokemonId = changes.pokemon.currentValue.pokemon.id;
    this.setMovesList(this.pokemonService.pokemonDetails$.value);
  }

  setMovesList(data) {
    if (this.pokemonId === '') {
      return;
    }

    this.pokemonMovesList = data[this.pokemonId]['moves']
      .map(move => {
        const label = `${move['name']} (${move['type']}, ${move['category']})`;
        return Object.assign({}, move, {'label': label});
      });
  }

  track(index, move) {
    return index;
  }


  get selected() {
    if (this.pokemonId === '') {
      return;
    }
    return this.pokemonId;
  }

  set selected(pokemon) {
    if (pokemon === null) {
      this.pokemonId = '';
      this.emitDefinitionChange([]);
      return;
    }
    this.pokemonId = pokemon;
    this.emitDefinitionChange([pokemon]);
    // Would it make sense to emit new Pokemon with all the
    // old moves? They might have some in common
  }

  moveChanged($event) {
    const moves = this.pokemon.moves
      .map(move => move.id);
    moves[$event.position] = $event.new;

    this.emitDefinitionChange([this.pokemon.pokemon.id].concat(moves));
  }

  emitDefinitionChange(newDefinition) {
    const oldDefinition = [this.pokemon.pokemon.id]
      .concat(this.pokemon.moves.map(move => move.id));
    const message = {
      'position': this.position,
      'old': oldDefinition,
      'new': newDefinition
    };

    this.pokemonChanged.emit(message);
  }
}
