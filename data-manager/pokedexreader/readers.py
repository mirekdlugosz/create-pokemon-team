"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2018  Mirosław Zalewski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

import sqlite3
from .constants import Constants


class EeveeReader():
    def __init__(self, path):
        self._pokedex = None
        self._id_pokemon_mapping = {}
        self._types = Constants.types
        self._versions = Constants.known_versions
        self._missing_moves_map = Constants.eeveedex_missing_moves
        self._querydb = {
            "fetch_all_moves": Constants.eeveedex_query_fetch_all_moves,
            "fetch_all_pokemon": Constants.eeveedex_query_fetch_all_pokemon,
            "fetch_pokemon_moves": Constants.eeveedex_query_fetch_pokemon_moves,
            "fetch_pokemon_types": Constants.eeveedex_query_fetch_pokemon_types,
            "fetch_all_moves_with_version": Constants.eeveedex_query_fetch_all_moves_with_version,
        }
        self._init_db_connection(path)
        self._fill_hidden_powers()
        self._fill_natural_gifts()

    def _init_db_connection(self, path):
        self._db_conn = sqlite3.connect(path)
        self._db_conn.row_factory = sqlite3.Row

    def _fill_hidden_powers(self):
        self._hidden_powers = []
        for move_type in [i for i in self._types if i not in ['Normal', 'Fairy']]:
            struct = {
                "move_identifier": 'hidden-power-{}'.format(move_type.lower()),
                "type": move_type,
                "category": 'special',
                "move_name": 'Hidden Power {}'.format(move_type),
            }
            self._hidden_powers.append(struct)

    def _fill_natural_gifts(self):
        self._natural_gifts = []
        for move_type in self._types:
            struct = {
                "move_identifier": 'natural-gift-{}'.format(move_type.lower()),
                "type": move_type,
                "category": 'physical',
                "move_name": "Natural Gift {}".format(move_type),
            }
            self._natural_gifts.append(struct)

    def _fetch_all_pokemon(self):
        return self._db_conn.execute(self._querydb["fetch_all_pokemon"]).fetchall()

    def _fetch_all_moves(self):
        return self._db_conn.execute(self._querydb["fetch_all_moves"]).fetchall()

    def _fetch_all_moves_with_version(self):
        return self._db_conn.execute(self._querydb["fetch_all_moves_with_version"]).fetchall()

    def _fetch_pokemon_types(self, pokemon_data_row):
        pokemon_id = pokemon_data_row["pokemon_form_identifier"]
        if ('arceus' in pokemon_id or 'silvally' in pokemon_id):
            return [pokemon_id.split('-')[1].title()]

        query = self._querydb["fetch_pokemon_types"].format(pokemon_data_row["pokemon_numeric_id"])
        return [row["name"] for row in self._db_conn.execute(query)]

    def _fetch_pokemon_moves(self, pokemon_id):
        group = next((group for group in Constants.eeveedex_equivalent_movesets
                      if pokemon_id in group), None)
        if group:
            pokemon_id = ",".join(group)

        query = self._querydb["fetch_pokemon_moves"].format(pokemon_id)
        return self._db_conn.execute(query).fetchall()

    def _ignore_pokemon(self, pokemon_data_row):
        pokemon_id = pokemon_data_row["pokemon_id"]
        return ("-totem" in pokemon_id
                or "pikachu-" in pokemon_id
                or "greninja-" in pokemon_id
                or "pichu-spiky-eared" == pokemon_data_row["pokemon_form_identifier"]
                or "rockruff-own-tempo" == pokemon_id
                or "floette-eternal" == pokemon_id
                or "arceus-unknown" == pokemon_data_row["pokemon_form_identifier"])

    def _get_real_pokemon_id(self, pokemon_data_row):
        current_id = pokemon_data_row["pokemon_form_identifier"]
        pokemon_id_parts = current_id.split("-", 1)
        if pokemon_id_parts[0] == current_id:
            return current_id

        if pokemon_id_parts[0] in Constants.eeveedex_equivalent_pokemon_ids:
            return pokemon_id_parts[0]
        return current_id

    def _create_pokemon_name(self, pokemon_data_row):
        if "silvally" in pokemon_data_row['pokemon_form_identifier']:
            return "Silvally ({} Type)".format(
                pokemon_data_row['pokemon_form_form_identifier'].capitalize())

        if not pokemon_data_row["pokemon_form_pokemon_name"]:
            return pokemon_data_row["pokemon_species_name"]

        if [i for i in Constants.eeveedex_equivalent_pokemon_ids
                if i in pokemon_data_row["pokemon_id"]]:
            return pokemon_data_row["pokemon_species_name"]

        if ("mega" in pokemon_data_row["pokemon_form_form_identifier"]
                or "alola" == pokemon_data_row["pokemon_form_form_identifier"]):
            return pokemon_data_row["pokemon_form_pokemon_name"]

        return "{} ({})".format(
            pokemon_data_row["pokemon_species_name"],
            pokemon_data_row["pokemon_form_name"]
        )

    def _get_prevolution(self, pokemon_id, evolves_from_numeric_id):
        if not evolves_from_numeric_id:
            return None

        if pokemon_id in Constants.eeveedex_evolves_from_override:
            return Constants.eeveedex_evolves_from_override[pokemon_id]

        if '-mega' in pokemon_id or '-primal' in pokemon_id:
            return pokemon_id.split('-', 1)[0]

        return self._id_pokemon_mapping[evolves_from_numeric_id]

    def _get_moves_in_version(self, moves, version):
        wanted_versions = self._versions[:self._versions.index(version) + 1]
        known_moves = [move["move_id"] for move in moves if move["version"] in wanted_versions]
        return sorted(list(set(known_moves)))

    def _expand_hidden_powers(self, moves):
        try:
            where = moves.index('hidden-power')
        except ValueError:
            return moves

        hidden_power_names = [move["move_identifier"] for move in self._hidden_powers]
        moves[where:where + 1] = hidden_power_names
        return moves

    def _expand_natural_gifts(self, moves, version):
        try:
            where = moves.index('natural-gift')
        except ValueError:
            return moves

        skip = ''
        if version in self._versions[:self._versions.index('x-y')]:
            skip = 'Fairy'

        natural_gifts_names = [move["move_identifier"] for move in
                self._natural_gifts if move["type"] != skip]

        moves[where:where + 1] = natural_gifts_names
        return moves

    def fill_pokedex(self, pokedex):
        self._pokedex = pokedex
        all_pokemon = self._fetch_all_pokemon()
        all_moves = self._fetch_all_moves() + self._hidden_powers + self._natural_gifts
        all_moves_with_version = self._fetch_all_moves_with_version()

        for pokemon_data_row in all_pokemon:
            if self._ignore_pokemon(pokemon_data_row):
                continue

            pokemon = {
                "pokemon_id": self._get_real_pokemon_id(pokemon_data_row),
                "name": self._create_pokemon_name(pokemon_data_row),
                "introduced_in_version": pokemon_data_row["pokemon_form_introduced_in_version"],
                "pokemon_type": self._fetch_pokemon_types(pokemon_data_row),
            }

            if pokemon["pokemon_id"] in self._id_pokemon_mapping:
                continue

            self._id_pokemon_mapping.update({
                pokemon["pokemon_id"]: pokemon_data_row["pokemon_numeric_id"],
                pokemon_data_row["pokemon_numeric_id"]: pokemon["pokemon_id"],
            })
            self._pokedex.add_pokemon(**pokemon)

            pokemon_prevolution = self._get_prevolution(pokemon["pokemon_id"], pokemon_data_row["pokemon_evolves_from"])
            pokemon_moves = self._fetch_pokemon_moves(pokemon_data_row["pokemon_numeric_id"])

            for version in set([row["version"] for row in pokemon_moves]):
                moves = [row["move_id"] for row in pokemon_moves if row["version"] == version]

                if (pokemon["pokemon_id"] in self._missing_moves_map
                        and version in self._missing_moves_map[pokemon["pokemon_id"]]):
                    moves.extend(self._missing_moves_map[pokemon["pokemon_id"]][version])

                try:
                    moves.extend(self._pokedex.get_pokemon_moves(version, pokemon_prevolution))
                except (ValueError, KeyError):
                    pass

                if pokemon["pokemon_id"] == "smeargle":
                    moves = self._get_moves_in_version(all_moves_with_version, version)

                moves = self._expand_hidden_powers(moves)
                moves = self._expand_natural_gifts(moves, version)
                moves = sorted(set(moves))

                self._pokedex.add_pokemon_moves(version, pokemon["pokemon_id"], moves)

        for move_data_row in all_moves:
            move = {
                "move_id": move_data_row["move_identifier"],
                "move_type": move_data_row["type"].title(),
                "category": move_data_row["category"],
                "name": move_data_row["move_name"]
            }
            self._pokedex.add_move(**move)
