import { environment } from '../../environments/environment';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Version } from '../utils/version';

import { Subject, Observable } from 'rxjs';


@Injectable()
export class MovesService {
  private _version: string;
  private _moves = {};
  private _requestedMoves: any[] = [];

  private _movesSet$ = new Subject();

  public movesData$ = new Subject();

  constructor(private http: HttpClient) {
    // this.input.subscribe(data => this.movesRequestHandler(data)); // TODO:
    this._movesSet$.subscribe(d => this.pushMoves());
  }

  public movesRequestHandler(data) {
    this._version = data.version;
    this._requestedMoves = data.moves;

    const missingMoves = this._requestedMoves
      .filter(moveName => (!(moveName in this._moves) && moveName !== undefined));

    if (missingMoves.length > 0) {
      const url = `${environment.endpoint}moves`;

      this.http
        .post<any[]>(url, missingMoves)
        .subscribe(result => {
          Object.assign(this._moves, result);
          this._movesSet$.next(true);
        });
    } else {
      this._movesSet$.next(true);
    }
  }

  private pushMoves() {
    const struct = {};
    for (const moveName of this._requestedMoves) {
      const move = Object.assign({}, this._moves[moveName]);
      if (move['override'] !== undefined) {
        if (Version.isLesserOrEqual(this._version, move['override']['last_version'])) {
          move['type'] = move['override']['type'];
        }
        delete move['override'];
      }
      struct[moveName] = move;
    }
    this.movesData$.next(struct);
  }
}
