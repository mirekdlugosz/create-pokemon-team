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
import { Subject } from 'rxjs';
import { Title } from '@angular/platform-browser';

@Injectable({
  providedIn: 'root'
})
export class TitleService {
  public title$ = new Subject<string>();

  /**
   *
   */
  constructor(private titleService: Title) {}

  public setTitle(title) {
    let t = title ? title + ' – createPokémon.​team' : 'createPokémon.​team';
    this.titleService.setTitle(t);
    this.title$.next(t);
  }
}
