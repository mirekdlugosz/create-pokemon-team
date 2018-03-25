import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamPermalinkComponent } from './team-permalink.component';

describe('TeamPermalinkComponent', () => {
  let component: TeamPermalinkComponent;
  let fixture: ComponentFixture<TeamPermalinkComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeamPermalinkComponent ]
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
