import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PokemonTypeEffectComponent } from './pokemon-type-effect.component';

describe('PokemonTypeEffectComponent', () => {
  let component: PokemonTypeEffectComponent;
  let fixture: ComponentFixture<PokemonTypeEffectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PokemonTypeEffectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PokemonTypeEffectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
