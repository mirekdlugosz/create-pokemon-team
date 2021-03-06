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
        self._move_categories = ['physical', 'special', 'status']
        self._evolution_trees = {}

    @property
    def _inserted_versions(self):
        versions = set()
        for pokemon in self.pokemon.values():
            versions.update(set(pokemon.moves.keys()))
        return versions

    def _get_evolution_chain(self, pokemon_id):
        evo_chain = [pokemon_id]
        while True:
            prevo = self.pokemon[pokemon_id].prevolution_id
            if not prevo and pokemon_id.endswith("alola"):
                prevo, _, _ = pokemon_id.partition("alola")
            if not prevo:
                break
            evo_chain.append(prevo)
            pokemon_id = prevo

        return list(reversed(evo_chain))

    def _longest_unique_paths(self, tree):
        """Removes elements of list that are strict subset of another element

        Given list of lists, removes elements that are fully contained within
        any other element.
        Example: [[1], [1, 2]] -> [[1, 2]]
        """
        out = []
        for branch_key in sorted(tree, key=lambda x: len(x), reverse=True):
            if all(set(branch_key) - set(existing) for existing in out):
                out.append(branch_key)
        return out

    def _create_evolution_trees(self):
        evolution_chains = {}
        for pokemon_obj in self.pokemon.values():
            evo_chain = self._get_evolution_chain(pokemon_obj.id)
            family_number = self.pokemon[evo_chain[0]].number
            evolution_chains.setdefault(family_number, []).append(evo_chain)

        return {family_number: self._longest_unique_paths(tree)
                for family_number, tree in evolution_chains.items()}

    def _sorting_key(self, pokemon_id):
        prevo = self._get_evolution_chain(pokemon_id)[0]
        family_number = self.pokemon[prevo].number
        pokemon_numbers = [self.pokemon[pokemon_id].number
                           for chain in self._evolution_trees[family_number]
                           for pokemon_id in chain]
        for chain_number, chain in enumerate(self._evolution_trees[family_number]):
            if pokemon_id in chain:
                evolution_chain_index = chain.index(pokemon_id)
                break
        return (min(pokemon_numbers), evolution_chain_index, chain_number)

    def _output_pokemon(self, fh):
        struct = {}
        self._evolution_trees = self._create_evolution_trees()
        for version, pokemon_ids in Constants.available_pokemon.items():
            if version not in self._inserted_versions:
                continue
            pokemon_ids = sorted(
                pokemon_ids,
                key=lambda x: self._sorting_key(x)
            )
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
        for version, pokemon_list in Constants.available_pokemon.items():
            if version not in self._inserted_versions:
                continue
            all_pokemon_ids.update(pokemon_list)

        for pokemon_id in all_pokemon_ids:
            learnset = self.pokemon[pokemon_id].moves
            for version, moves_list in learnset.items():
                if pokemon_id not in Constants.available_pokemon[version]:
                    continue
                struct.setdefault(version, {})[pokemon_id] = sorted(moves_list)

        json.dump(struct, fh)

    def _output_moves(self, fh):
        json.dump(self.moves, fh)

    def add_pokemon(self, pokemon_id=None, name=None, types=None, number=None,
                    prevolution_id=None, moves=None):
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

    def add_move(self, move_id=None, move_type=None, category=None, name=None):
        move_struct = {
            "type": move_type,
            "category": category,
            "name": name
        }

        if move_id in Constants.move_type_overrides:
            move_struct["override"] = Constants.move_type_overrides[move_id]

        if move_id in Constants.moves_inheriting_type:
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
