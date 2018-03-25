import { TestBed, inject } from '@angular/core/testing';

import { TypeeffectivenessService } from './typeeffectiveness.service';

describe('TypeeffectivenessService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TypeeffectivenessService]
    });
  });

  it('should be created', inject([TypeeffectivenessService], (service: TypeeffectivenessService) => {
    expect(service).toBeTruthy();
  }));
});
