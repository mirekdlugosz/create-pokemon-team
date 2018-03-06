import pytest

import pokedexreader.storage


@pytest.fixture
def pokemon_model():
    return {'generation': 5,
            'pokemon_id': 'pikachu',
            'name': 'Pikachu',
            'pokemon_type': ['Electric']}


@pytest.fixture
def pokedex():
    return pokedexreader.storage.PokedexStorage()


class TestAdd():
    def test_pokemon_with_empty_generation(self, pokemon_model, pokedex):
        pokemon_model["generation"] = ""
        with pytest.raises(ValueError) as cm:
            pokedex.add_pokemon(**pokemon_model)
        assert str(cm.value) == 'Generation cannot be empty'

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
