import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamOverviewComponent } from './team-overview.component';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import { TeamService } from '../../services/team.service';
import { TypeEffectivenessService } from '../../services/typeeffectiveness.service';

class TeamServiceStub{}
class TypeEffectivenessServiceStub{}

describe('TeamOverviewComponent', () => {
  let component: TeamOverviewComponent;
  let fixture: ComponentFixture<TeamOverviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeamOverviewComponent ],
      schemas: [ NO_ERRORS_SCHEMA ],
      providers: [
        {provide: TeamService, useClass: TeamServiceStub},
        {provide: TypeEffectivenessService, useClass: TypeEffectivenessServiceStub}
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeamOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have one overview for each available type');

  it('should correctly apply dynamic class for type');

  //I specifically use the word bind on these because I do not want to simply test that the method return
  //the correct values.  It also needs to determine if the binding happens correctly because likely the 
  //methods currently in the component will be replaced with calls to a service
  it('should correctly bind number of resists');
  it('should correctly bind number of weak to');
  it('should correctly bind number of super effective moves');
  it('should correctly bind counter');

  it('should show "No" counter in warning color');
  it('should list counter pokemon');

});
