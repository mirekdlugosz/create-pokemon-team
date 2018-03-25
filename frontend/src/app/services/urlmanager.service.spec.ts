import { TestBed, inject } from '@angular/core/testing';

import { UrlmanagerService } from './urlmanager.service';

describe('UrlmanagerService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [UrlmanagerService]
    });
  });

  it('should be created', inject([UrlmanagerService], (service: UrlmanagerService) => {
    expect(service).toBeTruthy();
  }));
});
