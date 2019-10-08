import { TestBed, inject } from '@angular/core/testing';

import { TeamService } from './team.service';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import { UrlmanagerService } from './urlmanager.service';

class UrlManagerStub{}

describe('TeamService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TeamService{provide: UrlmanagerService, useClass: UrlManagerStub}],
      schemas: [ NO_ERRORS_SCHEMA ]
    });
  });

  it('should be created', inject([TeamService], (service: TeamService) => {
    expect(service).toBeTruthy();
  }));

  it('should update url when team changes');

  //TODO stub unit tests
});
