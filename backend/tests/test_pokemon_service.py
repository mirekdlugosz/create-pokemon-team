import unittest
import json
import random

from api import pokemon


class PokemonServiceTestCase(unittest.TestCase):

    def setUp(self):
        pokemon.app.config['TESTING'] = True
        self.app = pokemon.app.test_client()

    def test_pokemon_list_status(self):
        rv = self.app.get('/pokemon')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.mimetype, 'application/json')

    def test_pokemon_moves_status(self):
        rv = self.app.get('/pokemon/sandslash/moves')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.mimetype, 'application/json')

    def test_non_existing_pokemon_moves_status(self):
        rv = self.app.get('/pokemon/missingno/moves')
        self.assertEqual(rv.status_code, 404)
        self.assertEqual(rv.mimetype, 'application/json')

    def test_non_existing_url_status(self):
        rv = self.app.get('/pokemon/')
        self.assertEqual(rv.status_code, 404)
        self.assertEqual(rv.mimetype, 'application/json')

    def test_pokemon_number(self):
        rv = self.app.get('/pokemon')
        pokemon_list = json.loads(rv.data.decode("utf-8"))
        self.assertEqual(len(pokemon_list), 959)

    def test_pokemon_structure(self):
        rv = self.app.get('/pokemon')
        pokemon_list = json.loads(rv.data.decode("utf-8"))
        pokemon_object = random.choice(pokemon_list)

        self.assertIn("id", pokemon_object)
        self.assertIn("name", pokemon_object)
        self.assertIn("type", pokemon_object)
        self.assertIsInstance(pokemon_object["type"], list)

    def test_move_number(self):
        rv = self.app.get('/pokemon/escavalier/moves')
        pokemon_moves = json.loads(rv.data.decode("utf-8"))
        self.assertEqual(len(pokemon_moves), 76)

    def test_move_structure(self):
        rv = self.app.get('/pokemon/escavalier/moves')
        pokemon_moves = json.loads(rv.data.decode("utf-8"))
        move_object = random.choice(pokemon_moves)

        self.assertIn("category", move_object)
        self.assertIn("name", move_object)
        self.assertIn("type", move_object)

    def test_mega_has_the_same_moveset_as_normal(self):
        rv = self.app.get('/pokemon/altaria/moves')
        altaria_moves = json.loads(rv.data.decode("utf-8"))

        rv = self.app.get('/pokemon/altariamega/moves')
        mega_altaria_moves = json.loads(rv.data.decode("utf-8"))

        self.assertEqual(altaria_moves, mega_altaria_moves)

    def test_alola_has_different_moveset(self):
        rv = self.app.get('/pokemon/sandslash/moves')
        sandslash_moves = json.loads(rv.data.decode("utf-8"))

        rv = self.app.get('/pokemon/sandslashalola/moves')
        alola_sandslash_moves = json.loads(rv.data.decode("utf-8"))

        self.assertNotEqual(sandslash_moves, alola_sandslash_moves)

if __name__ == '__main__':
    unittest.main()
