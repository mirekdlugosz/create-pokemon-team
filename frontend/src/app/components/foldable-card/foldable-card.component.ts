import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-foldable-card',
  templateUrl: './foldable-card.component.html',
  styleUrls: ['./foldable-card.component.scss']
})
export class FoldableCardComponent implements OnInit {
  @Input()
  displayed = true;

  constructor() { }

  ngOnInit() {
  }

}
