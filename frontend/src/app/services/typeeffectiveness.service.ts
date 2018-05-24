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
import { TypeChart } from '../utils/typechart';

@Injectable()
export class TypeEffectivenessService {
  public typeChart;
  public availableTypes = [];

  constructor() { }

  versionSet(versionData) {
    if (versionData.version === undefined) {
      return;
    }
    this.typeChart = TypeChart.inVersion(versionData.version);
    this.availableTypes = Object.keys(this.typeChart);
  }

  moveEffect(moveType, defendingType) {
    // This shouldn't ever happen, but rarely does in very
    // special circumstances - and is immediately followed by
    // correct call anyway
    if (!(moveType in this.typeChart)) {
      return 1;
    }

    return defendingType.reduce((factor, type) => {
      return factor * this.typeChart[moveType][type];
    }, 1);
  }
}
