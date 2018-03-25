import { Component, OnInit } from '@angular/core';

import { TeamService } from '../../services/team.service';

@Component({
  selector: 'app-team-builder',
  templateUrl: './team-builder.component.html',
  styleUrls: ['./team-builder.component.scss']
})
export class TeamBuilderComponent implements OnInit {

  constructor(public team: TeamService) {  }

  ngOnInit() { }

  track(index, pokemon) {
    return index;
  }

  teamChange($event) {
    this.team.teamChanged$.next($event);
  }
}
