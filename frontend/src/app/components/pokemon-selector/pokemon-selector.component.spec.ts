import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PokemonSelectorComponent } from './pokemon-selector.component';
import { NO_ERRORS_SCHEMA, Injectable } from '@angular/core';
import { PokemonService } from '../../services/pokemon.service';
import { of } from 'rxjs';

class PokemonServiceStub {
  public availablePokemon$ = of([]);
  public pokemonDetails$ = of({});
}

describe('PokemonSelectorComponent', () => {
  let component: PokemonSelectorComponent;
  let fixture: ComponentFixture<PokemonSelectorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PokemonSelectorComponent ],
      schemas: [ NO_ERRORS_SCHEMA ],
      providers: [{provide: PokemonService, useClass: PokemonServiceStub}]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PokemonSelectorComponent);
    component = fixture.componentInstance;
    component.pokemon = {currentValue: { pokemon: {id: ''}}};
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should load pokemon in dropdown');

  it('should load moves once pokemon is selected');

  it('should clear moves when pokemon is changed');
});
