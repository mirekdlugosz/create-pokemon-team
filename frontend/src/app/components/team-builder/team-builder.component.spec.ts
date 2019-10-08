import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamBuilderComponent } from './team-builder.component';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import { TeamService } from '../../services/team.service';

class TeamServiceStub{}

describe('TeamBuilderComponent', () => {
  let component: TeamBuilderComponent;
  let fixture: ComponentFixture<TeamBuilderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeamBuilderComponent ],
      schemas: [ NO_ERRORS_SCHEMA ],
      providers: [ {provide: TeamService, useClass: TeamServiceStub}]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeamBuilderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display 6 pokemon selectors when team has 6');
});
