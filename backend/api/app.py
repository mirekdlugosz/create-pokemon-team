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
]

api = flask.Blueprint('api', APP_NAME)


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

    return {pokemon: sorted(list(moves)) for pokemon, moves in pokemon_moves.items() if moves}


@api.route('/pokemon')
def pokemon_dispatcher():
    version = flask.request.args.get('ver', KNOWN_VERSIONS[-1])
    requested_pokemon = flask.request.args.getlist('p')
    transferred = flask.request.args.get('transferred', False)

    if version not in KNOWN_VERSIONS:
        return handle_not_found()

    if not requested_pokemon:
        response = get_pokemon(version)
    else:
        response = get_pokemon_moves(version, requested_pokemon, transferred)

    if not response:
        return handle_not_found()

    return flask.make_response(flask.jsonify(response))


@api.route('/moves', methods=['GET', 'POST'])
def get_moves():
    wanted = flask.request.get_json()
    if not wanted:
        return handle_not_found()

    struct = {}
    for move in wanted:
        try:
            struct[move] = MOVES[move]
        except KeyError:
            pass

    if not struct:
        return handle_not_found()

    return flask.make_response(flask.jsonify(struct))


@api.after_request
def set_origin_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


def create(config_filename):
    app = flask.Flask(APP_NAME)
    app.config.from_object(config_filename)

    app.register_blueprint(api)
    app.register_error_handler(404, handle_not_found)

    return app
