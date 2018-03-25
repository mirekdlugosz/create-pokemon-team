import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

import { Subject } from 'rxjs';

import { Version } from '../utils/version';

@Injectable()
export class UrlmanagerService {
  private version: string;
  private transferred: boolean;
  private team: any[];

  public version$ = new Subject();
  public teamDefinition$ = new Subject();

  constructor(private router: Router) { }

  public paramsChanged(data) {
    const params = data.params;
    let teamDefinition;

    if (params.version !== undefined &&
      Version.ids.includes(params.version)) {
      this.version = params.version;
    } else {
      this.version = Version.latest;
    }

    if (params.transferred !== undefined &&
      (params.transferred === 'true' || params.transferred === '1')) {
      this.transferred = true;
    } else {
      this.transferred = false;
    }

    this.version$.next(this.version$data);

    // assume empty team when:
    // - team is not present in paramsMap
    // - team is not valid JSON string
    // - team is not array
    try {
      teamDefinition = JSON.parse(params.team);
      if (teamDefinition.constructor !== Array) {
        throw new Error('JSON data does not contain array');
      }
    } catch (e) {
      teamDefinition = [];
    }

    this.teamDefinition$.next(teamDefinition);
  }

  private get version$data() {
    return {'version': this.version, 'transferred': this.transferred};
  }

  public openURLWithParam(paramMap) {
    const currentParams = this.router.parseUrl(this.router.url)['queryParams'];
    if (paramMap['remove'] !== undefined) {
      delete currentParams[paramMap.param];
    } else {
      currentParams[paramMap.param] = paramMap.value;
    }
    this.router.navigate(['/index'], {queryParams: currentParams});
  }
}
