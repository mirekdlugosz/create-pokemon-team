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
import { UrlmanagerService } from '../../services/urlmanager.service';
import { Version } from '../../utils/version';

@Component({
  selector: 'app-version-selector',
  templateUrl: './version-selector.component.html',
  styleUrls: ['./version-selector.component.scss']
})
export class VersionSelectorComponent implements OnInit {
  private data;
  public versions = Version.VERSIONS;

  constructor(private urlmanager: UrlmanagerService) { }

  ngOnInit() {
    this.urlmanager.version$.subscribe(d => this.data = d);
  }

  get versionState() {
    if (this.data === undefined) {
      return;
    }
    return this.data.version;
  }

  set versionState(newVersion) {
    const message = {
      'param': 'version',
      'value': newVersion
    }
    this.urlmanager.openURLWithParam(message);
  }

  get transferredState() {
    if (this.data === undefined) {
      return;
    }
    return this.data.transferred;
  }

  set transferredState(newState) {
    const message = {
      'param': 'transferred',
      'value': newState
    };
    if (newState === false) {
      message['remove'] = true;
    }
    this.urlmanager.openURLWithParam(message);
  }

}
