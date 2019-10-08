import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PokemonTypeEffectComponent } from './pokemon-type-effect.component';
import { By } from '@angular/platform-browser';
import { NO_ERRORS_SCHEMA } from '@angular/core';
import { TypeEffectivenessService } from '../../../services/typeeffectiveness.service';

class TypeEffectivenessServiceStub{}

describe('PokemonTypeEffectComponent', () => {
  let component: PokemonTypeEffectComponent;
  let fixture: ComponentFixture<PokemonTypeEffectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PokemonTypeEffectComponent ],
      schemas: [ NO_ERRORS_SCHEMA ],
      providers: [{provide: TypeEffectivenessService, useClass: TypeEffectivenessServiceStub}]
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

  it('should correctly apply dynamic class for type', () => {
    // const de = fixture.debugElement;
    // const typeDe = de.query(By.css('poison'));
    // const typeElement: HTMLElement = typeDe.nativeElement;
    // expect(typeDe).not.toEqual(null);
    // expect(typeElement.textContent).toEqual('null');
  });

  it('should apply success class to effect for effective moves');
  it('should apply danger class to effect for non effective moves');
  it('should apply no class to effect for neutral moves');

  it('should show popovers explaining columns');

  //I specifically use the word bind on these because I do not want to simply test that the method return
  //the correct values.  It also needs to determine if the binding happens correctly because likely the 
  //methods currently in the component will be replaced with calls to a service
  it('should correctly bind effect value');
  it('should correctly bind number of super effective moves');
  it('should correctly bind number of normally effective moves');
  it('should correctly bind number of not very effective moves');
});
