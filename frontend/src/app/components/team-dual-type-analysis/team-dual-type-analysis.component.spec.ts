import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamDualTypeAnalysisComponent } from './team-dual-type-analysis.component';

describe('TeamDualTypeAnalysisComponent', () => {
  let component: TeamDualTypeAnalysisComponent;
  let fixture: ComponentFixture<TeamDualTypeAnalysisComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeamDualTypeAnalysisComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeamDualTypeAnalysisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
