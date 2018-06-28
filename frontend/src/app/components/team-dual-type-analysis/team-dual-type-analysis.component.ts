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

import { Component, OnInit, Input } from '@angular/core';
import { PokemonService } from '../../services/pokemon.service';
import { TeamService } from '../../services/team.service';
import { TypeEffectivenessService } from '../../services/typeeffectiveness.service';

@Component({
  selector: 'app-team-dual-type-analysis',
  templateUrl: './team-dual-type-analysis.component.html',
  styleUrls: ['./team-dual-type-analysis.component.scss']
})
export class TeamDualTypeAnalysisComponent implements OnInit {
  @Input()
  public analysis: string;

  private checkFunction;
  private _dualTypePokemonList = [];
  private _team = [];
  private _availablePokemonLength: number;

  constructor(
    private pokemonService: PokemonService,
    private teamService: TeamService,
    private typeEffectivenessService: TypeEffectivenessService
  ) { }

  ngOnInit() {
    if (this.analysis === 'SE') {
      this.checkFunction = this.isSEcheck;
    } else if (this.analysis === 'counter') {
      this.checkFunction = this.isCounterCheck;
    } else {
      this.checkFunction = function(types) {
        return false;
      };
    }
  }

  dualTypePokemonList() {
    const availablePokemon = this.pokemonService.availablePokemon$.getValue();
    
    if (availablePokemon.length === this._availablePokemonLength &&
      Object.is(this.teamService.team, this._team)) {
      return this._dualTypePokemonList;
    }

    this._availablePokemonLength = availablePokemon.length;
    this._team = this.teamService.team;
    this._dualTypePokemonList = [];

    availablePokemon
      .filter(pokemon => pokemon.type.length > 1)
      .filter(pokemon => ! this.checkFunction(pokemon.type))
      .forEach(pokemon => {
        const typeId = pokemon.type.slice().sort().join('');
        const targetElemIndex = this._dualTypePokemonList.findIndex(e => e.id === typeId);

        if (targetElemIndex === -1) {
          const struct = {
            'id': typeId,
            'types': pokemon.type.slice().sort(),
            'pokemon': [pokemon.name]
          }
          this._dualTypePokemonList.push(struct);
        } else {
          this._dualTypePokemonList[targetElemIndex].pokemon.push(pokemon.name);
        }
      });

    this._dualTypePokemonList.sort(this.pokemonListSort);

    return this._dualTypePokemonList;
  }

  isSEcheck(types) {
    return this.teamService.team
      .map(member => {
        return member.moves
          .filter(move => move.type !== '')
          .filter(move => move.category !== 'status')
          .map(move => {
            return this.typeEffectivenessService
              .moveEffect(move.type, types);
          })
          .some(effect => effect > 1);
      })
      .some(value => value === true);
  }

  isCounterCheck(types) {
    return this.teamService.team
      .map(member => {
        return types
          .filter(typeName => typeName !== 'Normal')
          .map(typeName => this.typeEffectivenessService.isCounter(member, typeName))
          .every(value => value === true);
      })
      .some(value => value === true);
  }

  pokemonListSort = (a, b) => {
    const compareLength = b.pokemon.length - a.pokemon.length;
    if (compareLength !== 0) {
      return compareLength;
    }

    const availableTypes = this.typeEffectivenessService.availableTypes;

    const firstType = availableTypes.indexOf(a.types[0]) - availableTypes.indexOf(b.types[0]);
    if (firstType !== 0) {
      return firstType;
    }
    return availableTypes.indexOf(a.types[1]) - availableTypes.indexOf(b.types[1]);
  }
}
