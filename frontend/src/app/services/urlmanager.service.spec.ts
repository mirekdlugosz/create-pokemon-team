import { TestBed, inject } from '@angular/core/testing';

import { UrlmanagerService } from './urlmanager.service';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import { RouterTestingModule } from '@angular/router/testing';

describe('UrlmanagerService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ RouterTestingModule ],
      providers: [UrlmanagerService],
      schemas: [ NO_ERRORS_SCHEMA ]
    });
  });

  it('should be created', inject([UrlmanagerService], (service: UrlmanagerService) => {
    expect(service).toBeTruthy();
  }));

  //TODO stub unit tests
});
