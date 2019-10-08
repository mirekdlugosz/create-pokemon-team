import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MoveSelectorComponent } from './move-selector.component';
import { NO_ERRORS_SCHEMA } from '@angular/core';

describe('MoveSelectorComponent', () => {
  let component: MoveSelectorComponent;
  let fixture: ComponentFixture<MoveSelectorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MoveSelectorComponent ],
      schemas: [ NO_ERRORS_SCHEMA ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MoveSelectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
