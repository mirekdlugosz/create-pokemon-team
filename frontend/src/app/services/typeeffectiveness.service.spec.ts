import { TestBed, getTestBed } from '@angular/core/testing';

import { TypeEffectivenessService } from './typeeffectiveness.service';
import { TypeChart } from '../utils/typechart';

fdescribe('TypeeffectivenessService', () => {
  let service;
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TypeEffectivenessService]
    });
    service = getTestBed().get(TypeEffectivenessService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  describe('versionSet()', () => {
    it('should not do anything if version is undefined', () => {
      spyOn(TypeChart, 'inVersion').and.returnValue({});
      service.versionSet({ version: undefined });
      expect(TypeChart.inVersion).toHaveBeenCalledTimes(0);
    });

    it('should call appropriate functions if version is defined', () => {
      spyOn(TypeChart, 'inVersion').and.returnValue({});
      service.versionSet({ version: 1 });
      expect(TypeChart.inVersion).toHaveBeenCalledTimes(1);
    });
  });

  describe('moveEffect()', () => {
    it('returns 1 if moveType is not found in typeChart', () => {
      service.typeChart = { 'Normal': { 'Normal': 2, 'Rock': .5 } };
      const result = service.moveEffect('FakeType', ['Normal']);
      expect(result).toBe(1);
    });

    it('returns correct factor based on defense type and move type', () => {
      service.typeChart = { 'Normal': { 'Normal': 2, 'Rock': 3 }, 'Electric': { 'Normal': 0, 'Rock': 0 } };
      const result = service.moveEffect('Normal', ['Rock']);
      expect(result).toBe(3);
      const resultTwo = service.moveEffect('Normal', ['Normal']);
      expect(resultTwo).toBe(2);
      const resultThree = service.moveEffect('Normal', ['Normal', 'Rock']);
      expect(resultThree).toBe(6);
    });
  });

  describe('isCounter()', () => {
    beforeEach(() => {
      service = new TypeEffectivenessService();
      spyOn(service, 'moveEffect').and.callFake(function (x) {
        if (x === 'effective') {
          return 2;
        } else {
          return 0;
        }
      });
    });

    it('returns false if does not resist', () => {
      const result = service.isCounter({
        pokemon: { type: '' },
        moves: [{ id: 1, category: 'category', type: 'effective' },
        { id: 2, category: 'category', type: 'effective' }]
      },
        'effective');
      expect(result).toBe(false);
    });

    it('returns false if does not have super effective move', () => {
      const result = service.isCounter({
        pokemon: { type: '' },
        moves: [{ id: 1, category: 'category', type: 'ineffective' },
        { id: 2, category: 'category', type: 'ineffective' }]
      },
        'ineffective');
      expect(result).toBe(false);
    });

    it('returns true if  resists and has super effective move', () => {
      const result = service.isCounter({
        pokemon: { type: '' },
        moves: [{ id: 1, category: 'category', type: 'effective' },
        { id: 1, category: 'category', type: 'effective' }]
      },
        'ineffective');
      expect(result).toBe(true);
    });
  });
});
