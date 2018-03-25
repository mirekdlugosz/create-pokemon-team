import { TestBed, inject } from '@angular/core/testing';

import { MovesService } from './moves.service';

describe('MovesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MovesService]
    });
  });

  it('should be created', inject([MovesService], (service: MovesService) => {
    expect(service).toBeTruthy();
  }));
});
