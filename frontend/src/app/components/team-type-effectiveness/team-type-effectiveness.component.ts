import { Component, OnInit } from '@angular/core';
import { TeamService } from '../../services/team.service';
import { TypeEffectivenessService } from '../../services/typeeffectiveness.service';

@Component({
  selector: 'app-team-type-effectiveness',
  templateUrl: './team-type-effectiveness.component.html',
  styleUrls: ['./team-type-effectiveness.component.scss']
})
export class TeamTypeEffectivenessComponent implements OnInit {
  private hiddenMembers = [];

  constructor(
    public team: TeamService,
    private typeEffectiveness: TypeEffectivenessService
  ) { }

  ngOnInit() {
  }

  isVisible(index) {
    return ! this.hiddenMembers.includes(index);
  }

  toggleMemberVisibility(index) {
    if (this.isVisible(index)) {
      this.hiddenMembers.push(index);
    } else {
      const removeIndex = this.hiddenMembers.indexOf(index);
      this.hiddenMembers.splice(removeIndex, 1);
    }
  }

  scrollToMember(index) {
    const element = document.querySelector('#team-member-' + index);
    if (element) {
      element.scrollIntoView({'behavior': 'smooth'});
    }
  }

}
