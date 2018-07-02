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

import { Component, OnInit } from '@angular/core';
import { TeamService } from '../../services/team.service';
import { TypeEffectivenessService } from '../../services/typeeffectiveness.service';

@Component({
  selector: 'app-team-overview',
  templateUrl: './team-overview.component.html',
  styleUrls: ['./team-overview.component.scss']
})
export class TeamOverviewComponent implements OnInit {
  constructor(
    private team: TeamService,
    public typeEffectiveness: TypeEffectivenessService
  ) { }

  ngOnInit() {
  }

  number_resists(typeName) {
    return this.team.team
      .filter(member => member.pokemon.id !== '')
      .map(member => {
        return this.typeEffectiveness
          .moveEffect(typeName, member.pokemon.type);
      })
      .filter(factor => factor < 1)
      .length;
  }

  number_weak_to(typeName) {
    return this.team.team
      .filter(member => member.pokemon.id !== '')
      .map(member => {
        return this.typeEffectiveness
          .moveEffect(typeName, member.pokemon.type);
      })
      .filter(factor => factor > 1)
      .length;
  }

  number_supereffective_moves(typeName) {
    const moves = this.team.team
      .filter(member => member.moves.length > 0)
      .map(member => member.moves.filter(move => move.id !== ''));

    return [].concat(...moves)
      .filter(move => move.category !== 'status')
      .map(move => {
        return this.typeEffectiveness
          .moveEffect(move.type, [typeName]);
      })
      .filter(factor => factor > 1)
      .length;
  }

  counters_list(typeName) {
    return this.team.team
      .filter(member => this.typeEffectiveness.isCounter(member, typeName))
      .map(member => member.pokemon.name);
  }

  counter_exists(typeName) {
    return this.counters_list(typeName).length > 0;
  }
}
