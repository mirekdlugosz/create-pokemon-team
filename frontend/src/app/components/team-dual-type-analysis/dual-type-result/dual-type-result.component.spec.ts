import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DualTypeResultComponent } from './dual-type-result.component';

describe('DualTypeResultComponent', () => {
  let component: DualTypeResultComponent;
  let fixture: ComponentFixture<DualTypeResultComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DualTypeResultComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DualTypeResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
