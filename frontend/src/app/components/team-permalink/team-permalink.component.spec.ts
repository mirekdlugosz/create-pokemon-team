import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamPermalinkComponent } from './team-permalink.component';
import { NO_ERRORS_SCHEMA } from '@angular/core';

describe('TeamPermalinkComponent', () => {
  let component: TeamPermalinkComponent;
  let fixture: ComponentFixture<TeamPermalinkComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeamPermalinkComponent ],
      schemas: [ NO_ERRORS_SCHEMA ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeamPermalinkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
