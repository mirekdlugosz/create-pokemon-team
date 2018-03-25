import { Component, OnInit, OnChanges, Input } from '@angular/core';
import { TypeEffectivenessService } from '../../../services/typeeffectiveness.service';

@Component({
  selector: 'app-pokemon-type-effect',
  templateUrl: './pokemon-type-effect.component.html',
  styleUrls: ['./pokemon-type-effect.component.scss']
})
export class PokemonTypeEffectComponent implements OnInit, OnChanges {
  private movesEffectiveness: number[];

  @Input()
  pokemon;

  @Input()
  typeName: string;

  constructor(private typeEffectiveness: TypeEffectivenessService) { }

  ngOnInit() {
  }

  ngOnChanges() {
    if (this.pokemon === undefined) {
      return;
    }

    this.movesEffectiveness = this.pokemon.moves
      .filter(move => move.type !== '')
      .filter(move => move.category !== 'status')
      .map(move => {
        return this.typeEffectiveness
          .moveEffect(move.type, [this.typeName]);
        }
      );
  }

  public get effect() {
    if (this.pokemon === undefined) {
      return 0;
    }
    return this.typeEffectiveness.moveEffect(this.typeName, this.pokemon.pokemon.type);
  }

  public get super_effective() {
    if (this.pokemon === undefined) {
      return 0;
    }
    return this.movesEffectiveness
      .filter(factor => factor > 1)
      .length;
  }

  public get neutral_effective() {
    if (this.pokemon === undefined) {
      return 0;
    }
    return this.movesEffectiveness
      .filter(factor => factor === 1)
      .length;
  }

  public get not_very_effective() {
    if (this.pokemon === undefined) {
      return 0;
    }
    return this.movesEffectiveness
      .filter(factor => factor < 1)
      .length;
  }
}
