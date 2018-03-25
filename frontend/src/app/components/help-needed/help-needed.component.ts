import { Component, OnInit } from '@angular/core';
import { LocalStorage } from 'ngx-store';

@Component({
  selector: 'app-help-needed',
  templateUrl: './help-needed.component.html',
  styleUrls: ['./help-needed.component.scss']
})
export class HelpNeededComponent implements OnInit {
  @LocalStorage()
  private helpVisible = true;    // information stored in cookie
  private helpDismissed = false; // information stored in memory until page reload

  constructor() { }

  ngOnInit() {
  }

  public get showHelp() {
    return ( this.helpVisible && ! this.helpDismissed );
  }

}
