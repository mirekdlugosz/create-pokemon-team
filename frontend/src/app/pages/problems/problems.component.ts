import { Component, OnInit } from '@angular/core';
import { TitleService } from '../../services/title.service';

@Component({
  selector: 'app-problems',
  templateUrl: './problems.component.html',
  styleUrls: ['./problems.component.scss']
})
export class ProblemsComponent implements OnInit {
  constructor(private titleService: TitleService) {}

  ngOnInit() {
    this.titleService.setTitle('Problems');
  }
}
