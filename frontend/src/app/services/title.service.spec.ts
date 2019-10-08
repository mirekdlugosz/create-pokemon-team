import { TestBed, inject } from '@angular/core/testing';

import { TitleService } from './title.service';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import { UrlmanagerService } from './urlmanager.service';

describe('TitleService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TitleService],
      schemas: [ NO_ERRORS_SCHEMA ]
    });
  });

  it('should be created', inject(
    [TitleService],
    (service: TitleService) => {
      expect(service).toBeTruthy();
    }
  ));

  //TODO stub unit tests
});
