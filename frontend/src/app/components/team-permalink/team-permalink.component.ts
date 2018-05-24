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

@Component({
  selector: 'app-team-permalink',
  templateUrl: './team-permalink.component.html',
  styleUrls: ['./team-permalink.component.scss']
})
export class TeamPermalinkComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  public get teamURL() {
    return decodeURI(window.location.href);
  }

}
