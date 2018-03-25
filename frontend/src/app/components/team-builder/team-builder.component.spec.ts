import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamBuilderComponent } from './team-builder.component';

describe('TeamBuilderComponent', () => {
  let component: TeamBuilderComponent;
  let fixture: ComponentFixture<TeamBuilderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeamBuilderComponent ]
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
});
