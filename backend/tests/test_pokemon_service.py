import unittest

from api import pokemon


class PokemonServiceTestCase(unittest.TestCase):

    def setUp(self):
        pokemon.app.config['TESTING'] = True
        self.app = pokemon.app.test_client()

    def test_pokemon_list_status(self):
        rv = self.app.get('/pokemon')
        self.assertEqual(rv.status_code, 200)

    def test_pokemon_moves_status(self):
        rv = self.app.get('/pokemon/sandslash/moves')
        self.assertEqual(rv.status_code, 200)

    def test_non_existing_pokemon_moves_status(self):
        rv = self.app.get('/pokemon/missingno/moves')
        self.assertEqual(rv.status_code, 404)

    def test_non_existing_url_status(self):
        rv = self.app.get('/pokemon/')
        self.assertEqual(rv.status_code, 404)

if __name__ == '__main__':
    unittest.main()
