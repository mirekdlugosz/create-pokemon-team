import { TestBed, inject } from '@angular/core/testing';

import { TitleService } from './urlmanager.service';

describe('TitleService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TitleService]
    });
  });

  it('should be created', inject(
    [UrlmanagerService],
    (service: UrlmanagerService) => {
      expect(service).toBeTruthy();
    }
  ));
});
