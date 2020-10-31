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
import random

from api import app

game_version = 'omega-ruby-alpha-sapphire'


def get_json(rv):
    return json.loads(rv.data.decode("utf-8"))


@pytest.fixture
def client():
    application = app.create('settings')
    return application.test_client()


def test_non_existing_url_status(client):
    with client.get('/pokedex') as rv:
        assert rv.status_code == 404
        assert rv.mimetype == 'application/json'
        assert "error" in get_json(rv)


class TestPokemon():
    def test_status(self, client):
        with client.get('/pokemon') as rv:
            assert rv.status_code == 200
            assert rv.mimetype == 'application/json'

    def test_number(self, client):
        with client.get('/pokemon') as rv:
            pokemon_list = get_json(rv)
            assert len(pokemon_list) == 730

    def test_number_all(self, client):
        with client.get('/pokemon?ver=ultra-sun-ultra-moon') as rv:
            pokemon_list = get_json(rv)
            assert len(pokemon_list) == 939

    def test_structure(self, client):
        with client.get(f'pokemon?ver={game_version}') as rv:
            pokemon_object = random.choice(get_json(rv))

        assert "id" in pokemon_object
        assert "name" in pokemon_object
        assert "type" in pokemon_object
        assert isinstance(pokemon_object["type"], list)

    def test_changed_type(self, client):
        old_version = 'red-blue'
        new_version = 'sun-moon'
        wanted_pokemon = 'jigglypuff'
        with client.get(f'/pokemon?ver={old_version}') as rv:
            old_pokemon = next((pokemon for pokemon in get_json(rv) if pokemon["id"] == wanted_pokemon))
        with client.get(f'/pokemon?ver={new_version}') as rv:
            new_pokemon = next((pokemon for pokemon in get_json(rv) if pokemon["id"] == wanted_pokemon))

        assert old_pokemon['type'] != new_pokemon['type']

    def test_unknown_version(self, client):
        game_version = "omega-sun-ultra-blue"
        with client.get(f'pokemon?ver={game_version}') as rv:
            assert rv.status_code == 404
            assert rv.mimetype == 'application/json'
            assert "error" in get_json(rv)


class TestLearnsets():
    def test_status(self, client):
        pokemon = 'sandslash'
        with client.get(f'pokemon?ver={game_version}&p={pokemon}') as rv:
            assert rv.status_code == 200
            assert rv.mimetype == 'application/json'

    def test_non_existing_status(self, client):
        pokemon = 'missingno'
        with client.get(f'pokemon?ver={game_version}&p={pokemon}') as rv:
            assert rv.status_code == 404
            assert rv.mimetype == 'application/json'
            assert "error" in get_json(rv)

    def test_number(self, client):
        pokemon = 'escavalier'
        with client.get(f'pokemon?ver={game_version}&p={pokemon}') as rv:
            pokemon_moves = get_json(rv)
            assert len(pokemon_moves[pokemon]) == 74

    def test_transferred(self, client):
        pokemon = 'espeon'
        with client.get(f'/pokemon?ver={game_version}&p={pokemon}') as rv:
            moves = next((moves for moves in get_json(rv).values()))

        with client.get(f'/pokemon?ver={game_version}&p={pokemon}&transferred=true') as rv:
            transferred_moves = next((moves for moves in get_json(rv).values()))

        assert len(moves) != len(transferred_moves)
        assert moves != transferred_moves
        assert 'zapcannon' in transferred_moves
        assert 'zapcannon' not in moves

    def test_unknown_version(self, client):
        pokemon = 'sandslash'
        game_version = "omega-sun-ultra-blue"
        with client.get(f'pokemon?p={pokemon}&ver={game_version}') as rv:
            assert rv.status_code == 404
            assert rv.mimetype == 'application/json'
            assert "error" in get_json(rv)

    def test_mega_is_the_same(self, client):
        normal = 'altaria'
        mega = f'{normal}mega'
        with client.get(f'/pokemon?ver={game_version}&p={normal}') as rv:
            moves = next((moves for moves in get_json(rv).values()))

        with client.get(f'/pokemon?ver={game_version}&p={mega}') as rv:
            mega_moves = next((moves for moves in get_json(rv).values()))

        assert moves == mega_moves

    def test_alola_is_different(self, client):
        game_version = 'sun-moon'
        normal = 'sandslash'
        alola = f'{normal}alola'
        with client.get(f'/pokemon?ver={game_version}&p={normal}') as rv:
            moves = next((moves for moves in get_json(rv).values()))

        with client.get(f'/pokemon?ver={game_version}&p={alola}') as rv:
            alola_moves = next((moves for moves in get_json(rv).values()))

        assert moves != alola_moves


class TestMoves():
    def test_status(self, client):
        data = ['fly']
        rv = client.post('/moves',
                         data=json.dumps(data),
                         content_type='application/json')
        assert rv.status_code == 200
        assert rv.mimetype == 'application/json'

    def test_get_status(self, client):
        with client.get('/moves') as rv:
            assert rv.status_code == 400
            assert "error" in get_json(rv)

    def test_number(self, client):
        data = ['fly']
        rv = client.post('/moves',
                         data=json.dumps(data),
                         content_type='application/json')
        moves_list = get_json(rv)
        assert len(moves_list) == len(data)

    def test_structure(self, client):
        data = ['fly']
        rv = client.post('/moves',
                         data=json.dumps(data),
                         content_type='application/json')
        move_object = next((value for value in get_json(rv).values()))

        assert "category" in move_object
        assert "name" in move_object
        assert "type" in move_object

    def test_empty_request(self, client):
        data = []
        rv = client.post('/moves',
                         data=json.dumps(data),
                         content_type='application/json')
        assert rv.status_code == 400
        assert rv.mimetype == 'application/json'
        assert "error" in get_json(rv)

    def test_dict_request(self, client):
        data = {"fly": ""}
        rv = client.post('/moves',
                         data=json.dumps(data),
                         content_type='application/json')
        assert rv.status_code == 400
        assert rv.mimetype == 'application/json'
        assert "error" in get_json(rv)

    def test_unknown(self, client):
        data = ['10000-pika-fly']
        rv = client.post('/moves',
                         data=json.dumps(data),
                         content_type='application/json')
        assert rv.status_code == 404
        assert rv.mimetype == 'application/json'
        assert "error" in get_json(rv)

    def test_same_twice(self, client):
        data = ['fly', 'fly']
        rv = client.post('/moves',
                         data=json.dumps(data),
                         content_type='application/json')
        moves_list = get_json(rv)
        assert len(moves_list) == len(set(data))

    def test_changed_type(self, client):
        data = ['sweetkiss']
        rv = client.post('/moves',
                         data=json.dumps(data),
                         content_type='application/json')
        move_object = next((move for move in get_json(rv).values()))

        assert "override" in move_object
        assert "last_version" in move_object["override"]
        assert "type" in move_object["override"]

    def test_variable_type(self, client):
        data = ['judgment']
        rv = client.post('/moves',
                         data=json.dumps(data),
                         content_type='application/json')
        move_object = next((move for move in get_json(rv).values()))

        assert "uses_pokemon_type" in move_object
