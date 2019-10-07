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


class PokedexStorage():
    def __init__(self):
        self.pokemon = {}        # dict of available Pokemon
        self.pokemon_moves = {}  # Pokemon move learnsets
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
        for pokemon, data in self.pokemon.items():
            introduced_in_version = data["introduced_in_version"]
            try:
                override_list = self._versions[
                    :self._versions.index(data["override"]['last_version']) + 1
                ]
            except KeyError:
                override_list = []

            for version in self._versions[self._versions.index(introduced_in_version):]:
                if (version in self._invalid_pokemon_version_map and
                        pokemon in self._invalid_pokemon_version_map[version]):
                    continue

                poke_struct = {
                    "id": pokemon,
                    "name": data["name"],
                    "type": data["type"],
                }
                if version in override_list:
                    poke_struct["type"] = data["override"]["type"]

                struct.setdefault(version, []).append(poke_struct)

        json.dump(struct, fh)

    def _output_learnsets(self, fh):
        json.dump(self.pokemon_moves, fh)

    def _output_moves(self, fh):
        json.dump(self.moves, fh)

    def add_pokemon(self, introduced_in_version=None, pokemon_id=None, name=None, pokemon_type=None):
        if not introduced_in_version:
            raise ValueError('Version in which Pokemon was introduced cannot be empty')

        if not isinstance(introduced_in_version, str) or introduced_in_version.isdigit():
            raise ValueError('Version in which Pokemon was introduced cannot be numeric')

        if not pokemon_id:
            raise ValueError('Pokemon ID cannot be empty')

        if not name:
            raise ValueError('Pokemon name cannot be empty')

        if not pokemon_type:
            raise ValueError('Pokemon Type cannot be empty')

        if set(pokemon_type) & self._types != set(pokemon_type):
            raise ValueError('Unknown Type in {}; must be one of {}'.format(pokemon_type, self._types))

        if pokemon_id in self.pokemon:
            return

        pokemon_struct = {
            "id": pokemon_id,
            "name": name,
            "type": pokemon_type,
            "introduced_in_version": introduced_in_version,
        }

        if pokemon_id in self._pokemon_type_overrides:
            pokemon_struct["override"] = self._pokemon_type_overrides[pokemon_id]

        self.pokemon[pokemon_id] = pokemon_struct

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

    def get_pokemon_moves(self, version=None, pokemon_id=None):
        if not version:
            raise ValueError('Version identifier cannot be empty')
        if not pokemon_id:
            raise ValueError('Pokemon identifier cannot be empty')
        if version not in self.pokemon_moves:
            raise ValueError('Unknown version {}'.format(version))
        if pokemon_id not in self.pokemon_moves[version]:
            raise ValueError('Unknown pokemon {} in version {}'.format(pokemon_id, version))

        return self.pokemon_moves[version][pokemon_id]

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
