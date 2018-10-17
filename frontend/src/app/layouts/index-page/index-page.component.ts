import { Component, OnInit } from '@angular/core';
import { TitleService } from '../../services/title.service';

@Component({
  selector: 'app-index-page',
  templateUrl: './index-page.component.html'
})
export class IndexPageComponent implements OnInit {
  title = 'createPokémon.​team';

  constructor(private titleService: TitleService) {}

  ngOnInit() {
    this.titleService.title$.subscribe(title => {
      if (title) {
        this.title = title + ' – createPokémon.​team';
      } else {
        this.title = 'createPokémon.​team';
      }
    });
  }

}
