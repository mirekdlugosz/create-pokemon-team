"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2018  Mirosław Zalewski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

import json
import sqlite3
from pathlib import Path
from .constants import Constants


class AbstractReader:
    def __init__(self, path):
        self._types = Constants.types
        self._versions = Constants.known_versions
        self._all_valid_pokemon = set([pokemon_id
                                       for pokemon_list in Constants.available_pokemon.values()
                                       for pokemon_id in pokemon_list])
        self._fill_hidden_powers()
        self._fill_natural_gifts()

    def _fill_hidden_powers(self):
        self._hidden_powers = []
        for move_type in [i for i in self._types if i not in ['Normal', 'Fairy']]:
            struct = {
                "move_identifier": 'hiddenpower{}'.format(move_type.lower()),
                "type": move_type,
                "category": 'special',
                "move_name": 'Hidden Power {}'.format(move_type),
            }
            self._hidden_powers.append(struct)

    def _fill_natural_gifts(self):
        self._natural_gifts = []
        for move_type in self._types:
            struct = {
                "move_identifier": 'naturalgift{}'.format(move_type.lower()),
                "type": move_type,
                "category": 'physical',
                "move_name": "Natural Gift {}".format(move_type),
            }
            self._natural_gifts.append(struct)

    def _expand_hidden_powers(self, moves):
        if 'hiddenpower' not in moves:
            return moves

        hidden_power_names = [move["move_identifier"]
                              for move in self._hidden_powers]
        moves.remove('hiddenpower')
        return moves.union(hidden_power_names)

    def _expand_natural_gifts(self, moves, version):
        if 'naturalgift' not in moves:
            return moves

        skip = ''
        if self._versions.index('x-y') > self._versions.index(version):
            skip = 'Fairy'

        natural_gifts_names = [move["move_identifier"]
                               for move in self._natural_gifts
                               if move["type"] != skip]

        moves.remove('naturalgift')
        return moves.union(natural_gifts_names)


class EeveeReader(AbstractReader):
    def __init__(self, path):
        super().__init__(path)
        self._number_name_map = {}
        self._name_number_map = {}
        self._name_dbrow_map = {}
        self.__prevolution_cache = {}
        self._missing_moves_map = Constants.eeveedex_missing_moves
        self._querydb = {
            "fetch_all_moves": Constants.eeveedex_query_fetch_all_moves,
            "fetch_all_pokemon": Constants.eeveedex_query_fetch_all_pokemon,
            "fetch_pokemon_moves": Constants.eeveedex_query_fetch_pokemon_moves,
            "fetch_pokemon_types": Constants.eeveedex_query_fetch_pokemon_types,
            "fetch_all_moves_with_version": Constants.eeveedex_query_fetch_all_moves_with_version,
        }
        self._init_db_connection(path)
        self._all_pokemon = self._fetch_all_pokemon()

    def _init_db_connection(self, path):
        self._db_conn = sqlite3.connect(path)
        self._db_conn.row_factory = sqlite3.Row

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

    def _fetch_pokemon_moves(self, pokemon_numeric_ids):
        fetch_ids = ",".join(map(str, pokemon_numeric_ids))

        group = next((group for group in Constants.eeveedex_equivalent_movesets
                      if fetch_ids in group), None)
        if group:
            fetch_ids = ",".join(group)

        query = self._querydb["fetch_pokemon_moves"].format(fetch_ids)
        return self._db_conn.execute(query).fetchall()

    def _ignore_pokemon(self, pokemon_data_row):
        pokemon_id = pokemon_data_row["pokemon_id"]
        return ("-totem" in pokemon_id
                or "pikachu-" in pokemon_id
                or "greninja-" in pokemon_id
                or "pichu-spiky-eared" == pokemon_data_row["pokemon_form_identifier"]
                or "rockruff-own-tempo" == pokemon_id
                or "floette-eternal" == pokemon_id
                or "arceus-unknown" == pokemon_data_row["pokemon_form_identifier"]
                or self._get_pokemon_id(pokemon_data_row) in self._name_number_map)

    def _get_pokemon_id(self, pokemon_data_row):
        current_id = pokemon_data_row["pokemon_form_identifier"]
        pokemon_id_parts = current_id.split("-", 1)
        if pokemon_id_parts[0] == current_id:
            return current_id

        if pokemon_id_parts[0] in Constants.equivalent_pokemon_ids:
            return pokemon_id_parts[0]
        return current_id

    def _get_external_id(self, pokemon_id):
        if pokemon_id is None:
            return None
        if pokemon_id in Constants.eeveedex_external_ids:
            return Constants.eeveedex_external_ids[pokemon_id]
        return pokemon_id.replace("-", "")

    def _create_pokemon_name(self, pokemon_data_row):
        if "silvally" in pokemon_data_row['pokemon_form_identifier']:
            return "Silvally ({} Type)".format(
                pokemon_data_row['pokemon_form_form_identifier'].capitalize())

        if not pokemon_data_row["pokemon_form_pokemon_name"]:
            return pokemon_data_row["pokemon_species_name"]

        if [i for i in Constants.equivalent_pokemon_ids
                if i in pokemon_data_row["pokemon_id"]]:
            return pokemon_data_row["pokemon_species_name"]

        if ("mega" in pokemon_data_row["pokemon_form_form_identifier"]
                or "alola" == pokemon_data_row["pokemon_form_form_identifier"]):
            return pokemon_data_row["pokemon_form_pokemon_name"]

        if pokemon_data_row["pokemon_species_name"] == "Rotom":
            return pokemon_data_row["pokemon_form_name"]

        if pokemon_data_row["pokemon_species_name"] == "Kyurem":
            form, name = pokemon_data_row["pokemon_form_name"].split()
            return "{} ({})".format(name, form)

        if pokemon_data_row["pokemon_species_name"] == "Hoopa":
            name, form = pokemon_data_row["pokemon_form_name"].split()
            return "{} ({})".format(name, form)

        if pokemon_data_row["pokemon_form_identifier"] == "necrozma-ultra":
            return "Necrozma (Ultra)"

        return "{} ({})".format(
            pokemon_data_row["pokemon_species_name"],
            pokemon_data_row["pokemon_form_name"]
        )

    def _get_prevolution(self, pokemon_id):
        if pokemon_id in self.__prevolution_cache:
            return self.__prevolution_cache[pokemon_id]

        prevo = None
        if pokemon_id in Constants.eeveedex_evolves_from_override:
            prevo = Constants.eeveedex_evolves_from_override[pokemon_id]

        if '-mega' in pokemon_id or '-primal' in pokemon_id:
            prevo = pokemon_id.split('-', 1)[0]

        evolves_from_numeric_id = self._all_pokemon[
            self._name_dbrow_map[pokemon_id]]["pokemon_evolves_from"]
        if not prevo and evolves_from_numeric_id is not None:
            prevo = self._number_name_map[evolves_from_numeric_id]

        self.__prevolution_cache[pokemon_id] = prevo
        return prevo

    def _get_all_prevolutions(self, pokemon_id):
        prevo = self._get_prevolution(pokemon_id)
        if prevo:
            return self._get_all_prevolutions(prevo) + [prevo]
        return []

    def _get_pokemon_moves(self, pokemon_id):
        out = {}
        evolution_chain = self._get_all_prevolutions(pokemon_id) + [pokemon_id]
        numeric_ids = [self._name_number_map[name] for name in evolution_chain]
        moves_rows = self._fetch_pokemon_moves(numeric_ids)
        for move_row in moves_rows:
            out.setdefault(move_row['version'], set()).update(
                [move_row['move_id']]
            )

        if pokemon_id == "smeargle":
            all_moves = self._fetch_all_moves_with_version()
            for version in out:
                wanted_versions = self._versions[:self._versions.index(version) + 1]
                moves = [row['move_id'] for row in all_moves
                         if (row['version'] in wanted_versions
                             and row['move_id'] not in Constants.invalid_smeargle_moves)]
                out[version] = set(moves)

        for version, moves_list in out.items():
            moves_list = set([move.replace('-', '') for move in moves_list])
            moves_list = self._expand_hidden_powers(moves_list)
            moves_list = self._expand_natural_gifts(moves_list, version)

            try:
                missing_moves = Constants.eeveedex_missing_moves[pokemon_id][version]
                moves_list.update(missing_moves)
            except KeyError:
                pass

            out[version] = moves_list

        return out

    def fill_pokedex(self, pokedex):
        self._pokedex = pokedex
        all_moves = self._fetch_all_moves() + self._hidden_powers + self._natural_gifts

        for row_number, pokemon_data_row in enumerate(self._all_pokemon):
            pokemon_id = self._get_pokemon_id(pokemon_data_row)
            pokemon_number = pokemon_data_row["pokemon_numeric_id"]

            if self._ignore_pokemon(pokemon_data_row):
                continue

            self._number_name_map[pokemon_number] = pokemon_id
            self._name_number_map[pokemon_id] = pokemon_number
            self._name_dbrow_map[pokemon_id] = row_number

            external_pokemon_id = self._get_external_id(pokemon_id)
            prevolution = self._get_external_id(self._get_prevolution(pokemon_id))

            pokemon_moves = self._get_pokemon_moves(pokemon_id)

            pokemon = {
                "pokemon_id": external_pokemon_id,
                "name": self._create_pokemon_name(pokemon_data_row),
                "types": self._fetch_pokemon_types(pokemon_data_row),
                "number": pokemon_data_row['pokemon_species_id'],
                "prevolution_id": prevolution,
                "moves": pokemon_moves,
            }

            self._pokedex.add_pokemon(**pokemon)

        for move_data_row in all_moves:
            move = {
                "move_id": move_data_row["move_identifier"].replace('-', ''),
                "move_type": move_data_row["type"].title(),
                "category": move_data_row["category"],
                "name": move_data_row["move_name"]
            }
            self._pokedex.add_move(**move)


class ShowdownReader(AbstractReader):
    def __init__(self, path):
        super().__init__(path)
        self._all_pokemon = self._fetch_all_pokemon(path)
        self._all_moves = self._fetch_all_moves(path)
        self._pokemon_moves_map = self._fetch_learnsets(path)
        self._ignored_versions = ["red-blue", "yellow", "gold-silver",
                                  "crystal"]
        self._pokemon_names_ids_map = self._create_pokemon_names_ids_map()

    def _fetch_all_pokemon(self, basedir_path):
        with open(Path(basedir_path).joinpath('pokedex.json')) as fh:
            data = json.load(fh)
        return data

    def _fetch_all_moves(self, basedir_path):
        with open(Path(basedir_path).joinpath('moves.json')) as fh:
            data = json.load(fh)
        return data

    def _fetch_learnsets(self, basedir_path):
        with open(Path(basedir_path).joinpath('learnsets.json')) as fh:
            data = json.load(fh)
        data = self._transform_learnsets(data)
        return data

    def _transform_learnsets(self, learnsets):
        """Changes Showdown learnsets map to one easier to work with

        Basically inverts pokemon->move->version to pokemon->version->move,
        losing some details in the process.
        """
        out = {}
        for pokemon in learnsets:
            if "learnset" not in learnsets[pokemon]:
                continue
            learnset = learnsets[pokemon]["learnset"]
            out[pokemon] = self._invert_learnset_map(learnset)

        return out

    def _invert_learnset_map(self, learnset):
        """Performs transformation for single Pokemon. See _transform_learnsets
        """
        out = {}
        for move, learning_opportunities in learnset.items():
            versions = self._learning_opportunities_to_versions(move, learning_opportunities)
            for version in versions:
                out.setdefault(version, set()).add(move)

        return out

    def _learning_opportunities_to_versions(self, move, learning_opportunities):
        versions = set()
        for item in learning_opportunities:
            generation = int(item[0])
            method = item[1]
            games = Constants.games_in_generation[generation]
            if method == "C":  # Showdown optimization trick, ignore it
                continue
            if method == "T":  # Tutor - often exclusive to last game in generation
                games = [games[-1]]
                if generation in Constants.tutor_moves_map:
                    for tutor_special_case in Constants.tutor_moves_map[generation]:
                        if move in tutor_special_case["moves"]:
                            games = tutor_special_case["games"]
                            break
            versions.update(games)
        return versions

    def _create_pokemon_names_ids_map(self):
        names_ids_map = {}
        for pokemon_id, pokemon_obj in self._all_pokemon.items():
            names_ids_map[pokemon_obj["name"]] = pokemon_id
        return names_ids_map

    def _create_pokemon_name(self, pokemon_id):
        if pokemon_id in Constants.showdown_correct_pokemon_names:
            return Constants.showdown_correct_pokemon_names[pokemon_id]

        pokemon_obj = self._all_pokemon[pokemon_id]
        species = pokemon_obj.get('name', None)
        base_species = pokemon_obj.get('baseSpecies', None)
        forme = pokemon_obj.get('forme', None)
        base_forme = pokemon_obj.get('baseForme', None)
        # standard Pokemon - just return species
        if not any([base_species, forme, base_forme]):
            return species

        # base forme that is the only one in app - treat as standard Pokemon
        if [pokemon for pokemon in Constants.equivalent_pokemon_ids
                if pokemon_id.startswith(pokemon)]:
            return species

        species_name = base_species or species
        forme_name = base_forme or forme

        if species_name in ("Meowstic", "Indeedee"):
            if forme_name == "M":
                forme_name = "Male"
            else:
                forme_name = "Female"

        if forme_name == "Alola":
            return f"Alolan {species_name}"
        if forme_name == "Galar":
            return f"Galarian {species_name}"
        if forme_name == "Primal":
            return f"{species_name} (Primal Reversion)"
        if forme_name.startswith("Mega"):
            _, _, version = forme_name.partition("-")
            return f"Mega {species_name} {version}".strip()
        if species_name.startswith(("Rotom", "Zacian", "Zamazenta")):
            return f"{forme_name} {species_name}"
        if species_name.startswith(("Kyurem", "Hoopa", "Meowstic", "Indeedee")):
            return f"{species_name} ({forme_name})"
        if species_name.startswith("Necrozma"):
            return f"{species_name} ({forme_name.replace('-', ' ')})"

        suffix = "Forme"
        if species_name.startswith(("Arceus", "Silvally")):
            suffix = "Type"
        elif species_name.startswith("Lycanroc"):
            suffix = "Form"
        elif species_name.startswith("Wormadam"):
            suffix = "Cloak"
        elif species_name.startswith("Genesect"):
            suffix = "Drive"
        elif species_name.startswith("Darmanitan"):
            suffix = "Mode"
        elif species_name.startswith("Oricorio"):
            suffix = "Style"
        pokemon_name = f"{species_name} ({forme_name} {suffix})"
        if "'" in pokemon_name:
            pokemon_name = pokemon_name.replace("'", "’")
        return pokemon_name

    def _get_smeargle_moves(self):
        all_moves = {}
        introduced_in_index = Constants.known_versions.index('gold-silver')
        for pokemon_id, learnset in self._pokemon_moves_map.items():
            if pokemon_id not in self._all_valid_pokemon:
                continue
            for version, moves in learnset.items():
                if introduced_in_index > Constants.known_versions.index(version):
                    continue
                all_moves.setdefault(version, set()).update(moves.difference(
                    set(Constants.invalid_smeargle_moves)
                ))
        return all_moves

    def _get_pokemon_moves(self, pokemon_id):
        try:
            all_moves = self._pokemon_moves_map[pokemon_id]
        except KeyError:
            all_moves = {}
        prevo = self._get_prevolution(pokemon_id)
        if prevo:
            prevo_moves = self._get_pokemon_moves(prevo)
            for version, moves in prevo_moves.items():
                all_moves.setdefault(version, set()).update(moves)
        if pokemon_id == "smeargle":
            all_moves = self._get_smeargle_moves()

        for version, moves in all_moves.items():
            moves = self._expand_hidden_powers(moves)
            moves = self._expand_natural_gifts(moves, version)
            all_moves[version] = moves
        return all_moves

    def _get_prevolution(self, pokemon_id):
        if pokemon_id in Constants.showdown_prevolution_override:
            return Constants.showdown_prevolution_override[pokemon_id]

        pokemon_obj = self._all_pokemon[pokemon_id]
        if "prevo" in pokemon_obj:
            prevo_name = pokemon_obj["prevo"]
            return self._pokemon_names_ids_map[prevo_name]
        if "baseSpecies" in pokemon_obj and (
                pokemon_obj.get("forme", None) not in ["Alola", "Galar"]):
            return pokemon_obj["baseSpecies"].lower().replace("’", "")

        return None

    def _ignore_move(self, move_obj):
        return "isZ" in move_obj

    def fill_pokedex(self, pokedex):
        for pokemon_id in self._all_pokemon:
            if pokemon_id not in self._all_valid_pokemon:
                continue

            name = self._create_pokemon_name(pokemon_id)
            types = self._all_pokemon[pokemon_id]['types']
            number = self._all_pokemon[pokemon_id]['num']
            prevolution_id = self._get_prevolution(pokemon_id)
            moves = self._get_pokemon_moves(pokemon_id)

            pokedex.add_pokemon(pokemon_id, name, types, number, prevolution_id, moves)

        for move_id, move_obj in self._all_moves.items():
            if self._ignore_move(move_obj):
                continue
            pokedex.add_move(move_id, move_obj["type"], move_obj["category"].lower(), move_obj["name"])
