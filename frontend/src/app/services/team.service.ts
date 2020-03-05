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

import { Injectable } from '@angular/core';
import { UrlmanagerService } from './urlmanager.service';

import { Subject } from 'rxjs';

@Injectable()
export class TeamService {
  private MAX_MEMBERS_NUMBER = 6;
  private MOVES_NUMBER = 4;
  private _teamDefinition: any[] = [];
  private moveTemplate = {'category': '', 'name': '', 'type': '', 'id': ''};
  private memberTemplate = {'pokemon': {'id': '', 'name': '', 'type': []},
    'moves': Array(this.MOVES_NUMBER).fill(this.moveTemplate)};
  private EeveeShowdownMap = {
    "arceus-normal": "arceus",
    "darmanitan-standard": "darmanitan",
    "darmanitanzengalar": "darmanitangalarzen",
    "deoxys-normal": "deoxys",
    "giratina-altered": "giratina",
    "lycanroc-midday": "lycanroc",
    "meloetta-aria": "meloetta",
    "meowstic-male": "meowstic",
    "meowstic-female": "meowsticf",
    "necrozma-dawn": "necrozmadawnwings",
    "necrozma-dusk": "necrozmaduskmane",
    "oricorio-baile": "oricorio",
    "shaymin-land": "shaymin",
    "silvally-normal": "silvally",
    "wormadam-plant": "wormadam",
  }

  public team: any[] = Array(this.MAX_MEMBERS_NUMBER);
  public teamDataRequest$ = new Subject();
  public teamChanged$ = new Subject();

  constructor(private urlmanager: UrlmanagerService) {
    this.teamChanged$.subscribe(d => this.openNewTeamPage(d));
  }

  public createTeamFromURL(data) {
    // Ensure team has max MAX_MEMBERS Pokemon and each Pokemon
    // has max MOVES_NUMBER moves
    this._teamDefinition = data
      .slice(0, this.MAX_MEMBERS_NUMBER)
      .map(member => {
        if (member.length === 0) {
          return {'name': '', 'moves': []};
        }
        return {'name': member[0], 'moves': member.slice(1, this.MOVES_NUMBER + 1)};
      });

    let newTeamDefinition = this.applyFilters(this._teamDefinition);

    const outdatedTeamDefinition = (
      JSON.stringify(this._teamDefinition) !== JSON.stringify(newTeamDefinition))

    if (outdatedTeamDefinition) {
      const message = {
        'param': 'team',
        'value': JSON.stringify(this.teamDefinitionToURLDefinition(newTeamDefinition))
      }
      this.urlmanager.openURLWithParam(message);
      return;
    }

    this.teamDataRequest$.next(this._teamDefinition
      .map(pokemon => pokemon.name)
      .filter((name, num, arr) => name !== '' && arr.indexOf(name) === num)
    );
  }

  public fillTeamData(data) {
    // Ensure each team member is in list of known Pokemon
    // and each move can be learned by Pokemon who claims to know it
    // Also, ensure that team has exactly MAX_MEMBERS_NUMBER members
    // and each member has exactly MOVES_NUMBER moves
    this.team = this._teamDefinition
      .map(member => {
        // member.name will be empty string if member was not defined in URL
        // member.name will not be in data if requested Pokemon is not present in requested version
        if (member.name === '' || data[member.name] === undefined) {
          return JSON.parse(JSON.stringify(this.memberTemplate));
        }
        const pokemon = data[member.name]['pokemon'];
        const knownMoves = data[member.name]['moves'].map(move => move.id);
        const moves = member.moves
          .filter(move => knownMoves.includes(move) || move === '')
          .map(move => data[member.name]['moves'][knownMoves.indexOf(move)])
          .concat(Array(this.MOVES_NUMBER).fill(undefined))
          .slice(0, this.MOVES_NUMBER)
          .map(move => ((move === undefined) ? this.moveTemplate : move));
        return {'pokemon': pokemon, 'moves': moves};
      })
      .concat(Array(this.MAX_MEMBERS_NUMBER).fill(JSON.parse(JSON.stringify(this.memberTemplate))))
      .slice(0, this.MAX_MEMBERS_NUMBER);
  }

  public get isEmpty() {
    return this.team
      .filter(member => member.pokemon.id !== '')
      .length === 0;
  }

  public previousMemberIndex(index) {
    for (let i = index - 1; i >= 0; i--) {
      if (this.teamMemberIsDefined(i)) {
        return i;
      }
    }
    return undefined;
  }

  public nextMemberIndex(index) {
    for (let i = index + 1; i <= this.MAX_MEMBERS_NUMBER; i++) {
      if (this.teamMemberIsDefined(i)) {
        return i;
      }
    }
    return undefined;
  }

  public previousMemberIsDefined(index) {
    return this.previousMemberIndex(index) !== undefined;
  }

  public nextMemberIsDefined(index) {
    return this.nextMemberIndex(index) !== undefined;
  }

  private applyFilters(team) {
    return team.map(member => {
      let filteredName = this.filterName(member.name);
      let filteredMoves = member.moves
        .map(move => move.replace(/-/g, ''));
      return {"name": filteredName, "moves": filteredMoves};
    });
  }

  private filterName(name) {
    if (name in this.EeveeShowdownMap) {
      return this.EeveeShowdownMap[name];
    }
    return name.replace(/-/g, '');
  }

  private teamMemberIsDefined(index) {
    return (this.team[index] !== undefined && this.team[index].pokemon.id !== '');
  }

  private teamDefinitionToURLDefinition(teamDefinition) {
    return teamDefinition
      .map(member => [].concat([member.name], member.moves))
      .map(member => ((member[0] === '') ? [] : member ));
  }

  private teamToURLDefinition() {
    return this.team
      .map(member => {
        const moves = member.moves
          .map(move => move.id);
        return [].concat([member.pokemon.id], moves);
      })
      .map(member => ((member[0] === '') ? [] : member ));
  }

  private teamDefinitionAfterChange(changeData) {
    let teamDefinition = this.teamToURLDefinition();
    teamDefinition[changeData.position] = changeData.new;

    teamDefinition = teamDefinition.map(member =>
      member.reduceRight((a, b) => ((b !== '' || a.length) ? [b, ...a] : a), [])
    ).reduceRight((a, b) => ((b.length || a.length) ? [b, ...a] : a), []);

    return teamDefinition;
  }

  private openNewTeamPage(data) {
    const newTeamDefinition = this.teamDefinitionAfterChange(data);
    const message = {
      'param': 'team',
      'value': JSON.stringify(newTeamDefinition)
    }
    this.urlmanager.openURLWithParam(message);
  }
}
