import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VersionSelectorComponent } from './version-selector.component';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import { UrlmanagerService } from '../../services/urlmanager.service';
import { of } from 'rxjs';

class UrlManagerStub{
  public version$ = of();
}

describe('VersionSelectorComponent', () => {
  let component: VersionSelectorComponent;
  let fixture: ComponentFixture<VersionSelectorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VersionSelectorComponent ],
      schemas: [ NO_ERRORS_SCHEMA ],
      providers: [{provide: UrlmanagerService, useClass: UrlManagerStub}]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VersionSelectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  //TODO stub unit tests
});
