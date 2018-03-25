import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamTypeEffectivenessComponent } from './team-type-effectiveness.component';

describe('TeamTypeEffectivenessComponent', () => {
  let component: TeamTypeEffectivenessComponent;
  let fixture: ComponentFixture<TeamTypeEffectivenessComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeamTypeEffectivenessComponent ]
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
});
