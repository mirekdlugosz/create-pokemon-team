import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MoveSelectorComponent } from './move-selector.component';

describe('MoveSelectorComponent', () => {
  let component: MoveSelectorComponent;
  let fixture: ComponentFixture<MoveSelectorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MoveSelectorComponent ]
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
