import unittest

import pokedexreader.storage


class PokedexAddPokemonTest(unittest.TestCase):
    def setUp(self):
        self.pokedex = pokedexreader.storage.PokedexStorage()
        self.pokemon = {'generation': 5,
                        'pokemon_id': 'pikachu',
                        'name': 'Pikachu',
                        'pokemon_type': ['Electric']}

    def test_pokemon_with_empty_generation(self):
        pokemon = self.pokemon
        pokemon["generation"] = ""
        with self.assertRaises(ValueError) as cm:
            self.pokedex.add_pokemon(**pokemon)
        self.assertEqual(str(cm.exception), 'Generation cannot be empty')

    def test_pokemon_with_empty_id(self):
        pokemon = self.pokemon
        pokemon["pokemon_id"] = ""
        with self.assertRaises(ValueError) as cm:
            self.pokedex.add_pokemon(**pokemon)
        self.assertEqual(str(cm.exception), 'Pokemon ID cannot be empty')

    def test_pokemon_with_empty_name(self):
        pokemon = self.pokemon
        pokemon["name"] = ""
        with self.assertRaises(ValueError) as cm:
            self.pokedex.add_pokemon(**pokemon)
        self.assertEqual(str(cm.exception), 'Pokemon name cannot be empty')

    def test_pokemon_with_empty_type(self):
        pokemon = self.pokemon
        pokemon["pokemon_type"] = []
        with self.assertRaises(ValueError) as cm:
            self.pokedex.add_pokemon(**pokemon)
        self.assertEqual(str(cm.exception), 'Pokemon Type cannot be empty')

    def test_pokemon_with_unknown_type(self):
        pokemon = self.pokemon
        pokemon["pokemon_type"] = ['Nuclear']
        with self.assertRaises(ValueError) as cm:
            self.pokedex.add_pokemon(**pokemon)
        self.assertIn('Unknown Type in', str(cm.exception))
