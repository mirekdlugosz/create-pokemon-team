import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-move-selector',
  templateUrl: './move-selector.component.html',
  styleUrls: ['./move-selector.component.scss']
})
export class MoveSelectorComponent implements OnInit {

  @Input()
  movesList;

  @Input()
  move;

  @Input()
  position: number;

  @Output()
  moveChanged = new EventEmitter();

  constructor() { }

  ngOnInit() { }

  get selected() {
    if (this.move === undefined || this.move.id === '') {
      return;
    }
    return this.move.id;
  }

  set selected(move) {
    const change = {
      'position': this.position,
      'new': move === null ? '' : move
    }

    this.moveChanged.emit(change);
  }
}
