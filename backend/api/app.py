"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2018  Mirosław Zalewski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

import pathlib

import flask

APP_NAME = 'pokemon_api'
DATA_DIRECTORY = pathlib.Path(__file__).resolve().parent.joinpath('data')

with DATA_DIRECTORY.joinpath('pokemon.json').open() as fh:
    POKEMON = flask.json.load(fh)

with DATA_DIRECTORY.joinpath('learnsets.json').open() as fh:
    LEARNSETS = flask.json.load(fh)

with DATA_DIRECTORY.joinpath('moves.json').open() as fh:
    MOVES = flask.json.load(fh)

KNOWN_VERSIONS = [
    "red-blue", "yellow", "gold-silver", "crystal", "ruby-sapphire",
    "emerald", "firered-leafgreen", "diamond-pearl", "platinum",
    "heartgold-soulsilver", "black-white", "black-2-white-2", "x-y",
    "omega-ruby-alpha-sapphire", "sun-moon", "ultra-sun-ultra-moon",
    "sword-shield", "brilliant-diamond-shining-pearl"
]

api = flask.Blueprint('api', APP_NAME)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {"error": {"message": self.message}}

    @classmethod
    def custom_error_handler(cls, error):
        response = flask.jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @classmethod
    def handle_404(cls, error=None):
        error = cls('No such resource', 404)
        return cls.custom_error_handler(error)

    @classmethod
    def handle_500(cls, error=None):
        error = cls('Internal server error', 500)
        return cls.custom_error_handler(error)


def handle_not_found(e=None):
    response_text = {"error": "404 - no such resource"}
    return flask.make_response(flask.jsonify(response_text), 404)


def get_pokemon(version=None):
    return POKEMON[version]


def get_pokemon_moves(version=None, pokemon_list=None, transferred=False):
    pokemon_moves = {}
    versions = [version]
    if transferred:
        versions = KNOWN_VERSIONS[:KNOWN_VERSIONS.index(version) + 1]

    for version in versions:
        for pokemon in pokemon_list:
            try:
                pokemon_moves.setdefault(pokemon, set()).update(LEARNSETS[version][pokemon])
            except KeyError:
                pass

    pokemon_moves = {pokemon: sorted(list(moves)) for pokemon, moves in pokemon_moves.items() if moves}

    if not pokemon_moves:
        raise InvalidUsage('Unrecognized Pokemon requested', 404)

    return pokemon_moves


@api.route('/pokemon')
def pokemon_dispatcher():
    version = flask.request.args.get('ver', KNOWN_VERSIONS[-1])
    requested_pokemon = flask.request.args.getlist('p')
    transferred = flask.request.args.get('transferred', False)

    if version not in KNOWN_VERSIONS:
        raise InvalidUsage(f'Unknown version "{version}"', 404)

    if not requested_pokemon:
        response = get_pokemon(version)
    else:
        response = get_pokemon_moves(version, requested_pokemon, transferred)

    return flask.make_response(flask.jsonify(response))


@api.route('/moves', methods=['GET', 'POST'])
def get_moves():
    wanted = flask.request.get_json()
    if not wanted or not isinstance(wanted, list):
        raise InvalidUsage('Please provide list of moves in request body', 400)

    struct = {}
    for move in wanted:
        try:
            struct[move] = MOVES[move]
        except KeyError:
            pass

    if not struct:
        raise InvalidUsage('Unrecognized moves requested', 404)

    return flask.make_response(flask.jsonify(struct))


@api.after_request
def set_origin_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


def create(config_filename):
    app = flask.Flask(APP_NAME)
    app.config.from_object(config_filename)

    app.register_blueprint(api)
    app.register_error_handler(InvalidUsage, InvalidUsage.custom_error_handler)
    app.register_error_handler(404, InvalidUsage.handle_404)
    app.register_error_handler(500, InvalidUsage.handle_500)

    return app
