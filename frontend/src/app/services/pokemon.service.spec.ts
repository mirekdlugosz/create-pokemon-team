import { TestBed, inject } from '@angular/core/testing';

import { PokemonService } from './pokemon.service';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import { MovesService } from './moves.service';

class MovesServiceStub{}
describe('PokemonService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [PokemonService, {provide: MovesService, useClass: MovesServiceStub}],
      schemas: [ NO_ERRORS_SCHEMA ]
    });
  });

  it('should be created', inject([PokemonService], (service: PokemonService) => {
    expect(service).toBeTruthy();
  }));

  //TODO stub unit tests
});
