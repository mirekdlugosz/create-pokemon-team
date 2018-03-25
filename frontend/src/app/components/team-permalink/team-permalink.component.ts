import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-team-permalink',
  templateUrl: './team-permalink.component.html',
  styleUrls: ['./team-permalink.component.scss']
})
export class TeamPermalinkComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  public get teamURL() {
    return decodeURI(window.location.href);
  }

}
