"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2018  Mirosław Zalewski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

import pytest
import json
import io

import pokedexreader.storage
import pokedexreader.constants


@pytest.fixture
def pokemon_model():
    return {'introduced_in_version': 'sun-moon',
            'pokemon_id': 'pikachu',
            'name': 'Pikachu',
            'pokemon_type': ['Electric']}


@pytest.fixture
def _file():
    return io.StringIO()


@pytest.fixture
def pokedex():
    return pokedexreader.storage.PokedexStorage()


class TestInternal():
    def test_versions_in_constants(self):
        """Verify duplicated version names are exactly the same in
        both places they appear in.
        """
        in_constants = pokedexreader.constants.Constants.known_versions
        in_valid_list = pokedexreader.constants.Constants.available_pokemon.keys()
        for one, two in zip(in_constants, in_valid_list):
            assert one == two

        assert set(in_constants) == set(in_valid_list)


class TestAdd():
    def test_pokemon_with_empty_introduced_in_version(self, pokemon_model, pokedex):
        pokemon_model["introduced_in_version"] = ""
        with pytest.raises(ValueError) as cm:
            pokedex.add_pokemon(**pokemon_model)
        assert str(cm.value) == 'Version in which Pokemon was introduced cannot be empty'

    def test_pokemon_with_empty_id(self, pokemon_model, pokedex):
        pokemon_model["pokemon_id"] = ""
        with pytest.raises(ValueError) as cm:
            pokedex.add_pokemon(**pokemon_model)
        assert str(cm.value) == 'Pokemon ID cannot be empty'

    def test_pokemon_with_empty_name(self, pokemon_model, pokedex):
        pokemon_model["name"] = ""
        with pytest.raises(ValueError) as cm:
            pokedex.add_pokemon(**pokemon_model)
        assert str(cm.value) == 'Pokemon name cannot be empty'

    def test_pokemon_with_empty_type(self, pokemon_model, pokedex):
        pokemon_model["pokemon_type"] = []
        with pytest.raises(ValueError) as cm:
            pokedex.add_pokemon(**pokemon_model)
        assert str(cm.value) == 'Pokemon Type cannot be empty'

    def test_pokemon_with_unknown_type(self, pokemon_model, pokedex):
        pokemon_model["pokemon_type"] = ['Nuclear']
        with pytest.raises(ValueError) as cm:
            pokedex.add_pokemon(**pokemon_model)
        assert 'Unknown Type in' in str(cm.value)

    def test_pokemon_with_lowercase_type(self, pokemon_model, pokedex):
        pokemon_model["pokemon_type"] = ["electric"]
        with pytest.raises(ValueError) as cm:
            pokedex.add_pokemon(**pokemon_model)
        assert 'Unknown Type in' in str(cm.value)


class TestOutput():
    def test_pokemon_structure(self, pokemon_model, pokedex, _file):
        pokedex.add_pokemon(**pokemon_model)
        expected = {
            "sun-moon": [
                {"id": "pikachu",
                 "name": "Pikachu",
                 "type": ["Electric"]},
            ],
            "ultra-sun-ultra-moon": [
                {"id": "pikachu",
                 "name": "Pikachu",
                 "type": ["Electric"]},
            ],
        }
        pokedex._output_pokemon(_file)
        _file.seek(0)

        assert _file.read() == json.dumps(expected)

    def test_pokemon_override_type(self, pokedex, _file):
        pokemon_model = {
            'introduced_in_version': 'red-blue',
            'pokemon_id': 'jigglypuff',
            'name': 'Jigglypuff',
            'pokemon_type': ['Normal', 'Fairy'],
        }
        pokedex.add_pokemon(**pokemon_model)
        pokedex._output_pokemon(_file)
        _file.seek(0)
        data = json.load(_file)

        assert data["red-blue"][0]["type"] == ['Normal']
        assert data["black-2-white-2"][0]["type"] == ['Normal']
        assert data["x-y"][0]["type"] == ['Normal', 'Fairy']
        assert data["sun-moon"][0]["type"] == ['Normal', 'Fairy']
