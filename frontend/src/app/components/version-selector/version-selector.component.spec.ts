import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VersionSelectorComponent } from './version-selector.component';

describe('VersionSelectorComponent', () => {
  let component: VersionSelectorComponent;
  let fixture: ComponentFixture<VersionSelectorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VersionSelectorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VersionSelectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
