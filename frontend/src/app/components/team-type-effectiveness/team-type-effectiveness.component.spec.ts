import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamTypeEffectivenessComponent } from './team-type-effectiveness.component';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import { TeamService } from '../../services/team.service';
import { TypeEffectivenessService } from '../../services/typeeffectiveness.service';

class TeamServiceStub{}
class TypeEffectivenessServiceStub{}

describe('TeamTypeEffectivenessComponent', () => {
  let component: TeamTypeEffectivenessComponent;
  let fixture: ComponentFixture<TeamTypeEffectivenessComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeamTypeEffectivenessComponent ],
      schemas: [ NO_ERRORS_SCHEMA ],
      providers: [
        {provide: TeamService, useClass: TeamServiceStub},
        {provide: TypeEffectivenessService, useClass: TypeEffectivenessServiceStub}
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeamTypeEffectivenessComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should show error message if team is empty');
  it('should show inner component once for each pokemon currently on team') //named this inner component for now but should probably apply a class so we can recognize it
  it('should show pokemon name above stats');
  it('should hide pokemon stats when name is clicked');
  it('should scroll to next team member when next is clicked');
  it('should scroll to previous team member when previous is clicked');
  it('should show only next and not previous on first pokemon');
  it('should show only previous and not next on last pokemon');
  it('should show both next and previous on middle pokemon');
  it('should not show previous or next when theres only one pokemon');
  it('should show pokemon type effect for each available type');

});
