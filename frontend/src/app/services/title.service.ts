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
import { Router } from '@angular/router';

import { Subject } from 'rxjs';

@Injectable()
export class TitleService {
  public title$ = new Subject<string>();

  constructor() {}

  public setTitle(title) {
    this.title$.next(title);
  }
}
