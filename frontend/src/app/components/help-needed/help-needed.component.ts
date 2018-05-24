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
import { LocalStorage } from 'ngx-store';

@Component({
  selector: 'app-help-needed',
  templateUrl: './help-needed.component.html',
  styleUrls: ['./help-needed.component.scss']
})
export class HelpNeededComponent implements OnInit {
  @LocalStorage()
  private helpVisible = true;    // information stored in cookie
  private helpDismissed = false; // information stored in memory until page reload

  constructor() { }

  ngOnInit() {
  }

  public get showHelp() {
    return ( this.helpVisible && ! this.helpDismissed );
  }

}
