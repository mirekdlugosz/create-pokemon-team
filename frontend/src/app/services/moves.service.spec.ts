import { TestBed, inject } from '@angular/core/testing';

import { MovesService } from './moves.service';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import {HttpClientTestingModule} from '@angular/common/http/testing';

describe('MovesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [MovesService],
      schemas: [ NO_ERRORS_SCHEMA ]
    });
  });

  it('should be created', inject([MovesService], (service: MovesService) => {
    expect(service).toBeTruthy();
  }));

  it('should call proper endpoint to load moves');
  it('should correctly override move');
  it('should emit moves dataset');
});
