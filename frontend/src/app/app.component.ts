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
import { Title } from '@angular/platform-browser'
import { Router, NavigationEnd } from '@angular/router';

const capitalize = ([s, ...tring]) => [s.toUpperCase(), ...tring].join('');
const setPageTitle = (url: string = ''): string => {
    const removedSlashedUrl = url.replace('/', '');
    const capTitle = capitalize(<any>removedSlashedUrl);
    return `${capTitle} - createPokémon.​team`
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent implements OnInit {
  private urlParser = document.createElement('a');
  private previousPage: string;

  constructor(
      private router: Router,
      private titleService: Title
  ) { }

  ngOnInit() {
    this.router.events.subscribe((evt) => {
      if (!(evt instanceof NavigationEnd)) {
        return;
      }

      this.titleService.setTitle(setPageTitle(evt.url));

      this.urlParser.href = evt.url;
      if (this.urlParser.pathname === '/') {
        this.urlParser.pathname = '/index';
      }

      if (this.urlParser.pathname === this.previousPage) {
        return;
      }
      window.scrollTo(0, 0);
      this.previousPage = this.urlParser.pathname;
    });
  }
}
