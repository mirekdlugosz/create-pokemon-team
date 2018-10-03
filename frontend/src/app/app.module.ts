/**
 * createPokémon.team - web application that helps you build your own
 * Pokémon team in any core series game
 * Copyright © 2018  Mirosław Zalewski
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * any later version.
 */

// core angular modules
import { BrowserModule } from '@angular/platform-browser';
import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

// third-party modules
import { FormsModule } from '@angular/forms';
import { NgSelectModule } from '@ng-select/ng-select';
import { WebStorageModule } from 'ngx-store';
import { ClipboardModule } from 'ngx-clipboard';

// layouts
import { IndexPageComponent } from './layouts/index-page/index-page.component';
import { StaticPageComponent } from './layouts/static-page/static-page.component';

// pages
import { IndexComponent } from './pages/index/index.component';
import { AboutComponent } from './pages/about/about.component';
import { HelpComponent } from './pages/help/help.component';
import { LegalComponent } from './pages/legal/legal.component';
import { ProblemsComponent } from './pages/problems/problems.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';

// custom components
import { AppComponent } from './app.component';
import { VersionSelectorComponent } from './components/version-selector/version-selector.component';
import { TeamBuilderComponent } from './components/team-builder/team-builder.component';
import { PokemonSelectorComponent } from './components/pokemon-selector/pokemon-selector.component';
import { MoveSelectorComponent } from './components/pokemon-selector/move-selector/move-selector.component';
import { HelpNeededComponent } from './components/help-needed/help-needed.component';
import { FoldableCardComponent } from './components/foldable-card/foldable-card.component';
import { TeamTypeEffectivenessComponent } from './components/team-type-effectiveness/team-type-effectiveness.component';
import { PokemonTypeEffectComponent } from './components/team-type-effectiveness/pokemon-type-effect/pokemon-type-effect.component';
import { TeamOverviewComponent } from './components/team-overview/team-overview.component';
import { TeamPermalinkComponent } from './components/team-permalink/team-permalink.component';

// services
import { UrlmanagerService } from './services/urlmanager.service';
import { TeamService } from './services/team.service';
import { PokemonService } from './services/pokemon.service';
import { MovesService } from './services/moves.service';
import { TypeEffectivenessService } from './services/typeeffectiveness.service';
import { TitleService } from './services/title.service';

export const ROUTETABLE: Routes = [
  { path: '', pathMatch: 'full', redirectTo: '/index' },
  {
    path: '',
    component: IndexPageComponent,
    children: [
      { path: 'index', component: IndexComponent },
      {path: '',
        component: StaticPageComponent,
        children: [
          {path: 'about', component: AboutComponent },
          {path: 'help', component: HelpComponent },
          {path: 'legal', component: LegalComponent },
          {path: 'problems', component: ProblemsComponent }
        ]
      }
    ]
  },
  { path: '**', component: PageNotFoundComponent }
];

@NgModule({
  declarations: [
    IndexPageComponent,
    StaticPageComponent,
    IndexComponent,
    AboutComponent,
    HelpComponent,
    LegalComponent,
    ProblemsComponent,
    PageNotFoundComponent,
    AppComponent,
    VersionSelectorComponent,
    TeamBuilderComponent,
    PokemonSelectorComponent,
    MoveSelectorComponent,
    HelpNeededComponent,
    TeamTypeEffectivenessComponent,
    PokemonTypeEffectComponent,
    TeamOverviewComponent,
    FoldableCardComponent,
    TeamPermalinkComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(ROUTETABLE),
    HttpClientModule,
    FormsModule,
    NgSelectModule,
    WebStorageModule,
    ClipboardModule
  ],
  providers: [
    UrlmanagerService,
    TeamService,
    PokemonService,
    MovesService,
    TypeEffectivenessService,
    TitleService
  ],
  bootstrap: [AppComponent],
  schemas: [NO_ERRORS_SCHEMA]
})
export class AppModule {}
