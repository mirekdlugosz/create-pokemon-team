"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2018  Mirosław Zalewski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

import sys
import pathlib
import json
from .constants import Constants


class Pokemon():
    def __init__(self, pokemon_id=None, name=None, types=None,
                 number=None, prevolution_id=None, moves=None):
        self.id = pokemon_id
        self.name = name
        self._type = types
        self.number = number
        self.prevolution_id = prevolution_id
        self.moves = moves or {}
        self.override = None

        try:
            self.override = Constants.pokemon_type_overrides[pokemon_id]
        except KeyError:
            pass

    def type(self, version):
        if self.override:
            max_index = Constants.known_versions.index(self.override["last_version"])
            index = Constants.known_versions.index(version)
            if max_index >= index:
                return self.override["type"]

        return self._type

    def update(self, **kwargs):
        for arg, value in kwargs.items():
            if arg == "moves":
                self._update_moves(value)
                continue
            if arg == "types":
                arg = "_type"
            current_value = getattr(self, arg)
            if value != current_value:
                print(f"{self.id}: setting {arg} to {value} (was {current_value})")
            setattr(self, arg, value)

    def _update_moves(self, moves):
        for version, learnset in moves.items():
            self.moves.setdefault(version, set()).update(learnset)


class PokedexStorage():
    def __init__(self):
        self.pokemon = {}        # dict of available Pokemon
        self.moves = {}          # move information
        self._types = Constants.types
        self._versions = Constants.known_versions
        self._move_categories = ['physical', 'special', 'status']
        self._move_type_overrides = Constants.move_type_overrides
        self._moves_inheriting_type = Constants.moves_inheriting_type
        self._pokemon_type_overrides = Constants.pokemon_type_overrides
        self._invalid_pokemon_version_map = Constants.invalid_pokemon_version

    def _output_pokemon(self, fh):
        struct = {}
        for version, pokemon_ids in Constants.available_pokemon.items():
            # odpowiednie sortowanie
            for pokemon_id in pokemon_ids:
                pokemon_obj = self.pokemon[pokemon_id]
                poke_struct = {
                    "id": pokemon_obj.id,
                    "name": pokemon_obj.name,
                    "type": pokemon_obj.type(version),
                }
                struct.setdefault(version, []).append(poke_struct)

        json.dump(struct, fh)

    def _output_learnsets(self, fh):
        struct = {}
        all_pokemon_ids = set()
        for pokemon_list in Constants.available_pokemon.values():
            all_pokemon_ids.update(pokemon_list)

        for pokemon_id in pokemon_list:
            learnset = self.pokemon[pokemon_id].moves
            for version, moves_list in learnset.items():
                struct.setdefault(version, {})[pokemon_id] = sorted(moves_list)

        json.dump(struct, fh)

    def _output_moves(self, fh):
        json.dump(self.moves, fh)

    def add_pokemon(self, pokemon_id=None, name=None, types=None, number=None,
                    prevolution_id=None, moves=None):
        """
        if not pokemon_id:
            raise ValueError('Pokemon ID cannot be empty')

        if not name:
            raise ValueError('Pokemon name cannot be empty')

        if not types:
            raise ValueError('Pokemon Type cannot be empty')

        if set(types) & self._types != set(types):
            raise ValueError('Unknown Type in {}; must be one of {}'.format(types, self._types))
        """

        kwargs = {
            "name": name,
            "types": types,
            "number": number,
            "prevolution_id": prevolution_id,
            "moves": moves,
        }

        try:
            self.pokemon[pokemon_id].update(**kwargs)
        except KeyError:
            self.pokemon[pokemon_id] = Pokemon(pokemon_id=pokemon_id, **kwargs)

    def add_pokemon_moves(self, version=None, pokemon_id=None, moves=None):
        if not version:
            raise ValueError('Version identifier cannot be empty')
        if not pokemon_id:
            raise ValueError('Pokemon identifier cannot be empty')
        if not moves:
            raise ValueError('Pokemon moves must be non-empty list')

        self.pokemon_moves.setdefault(version, {}).setdefault(pokemon_id, []).extend(moves)

    def add_move(self, move_id=None, move_type=None, category=None, name=None):
        if not move_id:
            raise ValueError('Move ID cannot be empty')

        if not isinstance(move_id, str) or move_id.isdigit():
            raise ValueError('Move ID cannot be numeric')

        if not move_type:
            raise ValueError('Move type cannot be empty')

        if move_type not in self._types:
            raise ValueError('Unknown type in {}; must be one of {}'.format(move_type, self._types))

        if not category:
            raise ValueError('Move category cannot be empty')

        if category not in self._move_categories:
            raise ValueError('Unknown category in {}; must be one of {}'.format(category, self._move_categories))

        if not name:
            raise ValueError('Move name cannot be empty')

        move_struct = {
            "type": move_type,
            "category": category,
            "name": name
        }

        if move_id in self._move_type_overrides:
            move_struct["override"] = self._move_type_overrides[move_id]

        if move_id in self._moves_inheriting_type:
            move_struct["uses_pokemon_type"] = True

        self.moves[move_id] = move_struct

    def output(self, directory):
        if directory == '-':
            self._output_pokemon(sys.stdout)
            self._output_learnsets(sys.stdout)
            self._output_moves(sys.stdout)
        else:
            directory = pathlib.Path(directory)
            directory.mkdir(parents=True, exist_ok=True)
            with directory.joinpath("pokemon.json").open('w') as fh:
                self._output_pokemon(fh)
            with directory.joinpath("learnsets.json").open('w') as fh:
                self._output_learnsets(fh)
            with directory.joinpath("moves.json").open('w') as fh:
                self._output_moves(fh)

    def dump_data(self, data_to_dump, pretty):
        if pretty:
            import pprint
            pp = pprint.PrettyPrinter(compact=True)
            p = pp.pprint
        else:
            p = print
        if 'all' in data_to_dump:
            data_to_dump.extend(['pokemon', 'learnsets', 'moves'])
        if 'pokemon' in data_to_dump:
            p(self.pokemon)
        if 'learnsets' in data_to_dump:
            p(self.pokemon_moves)
        if 'moves' in data_to_dump:
            p(self.moves)
