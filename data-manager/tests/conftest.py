"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2019  Mirek Długosz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

import io
import json
import pytest

from pokedexreader.readers import EeveeReader, ShowdownReader
from pokedexreader.storage import PokedexStorage


def pytest_addoption(parser):
    parser.addoption('--eevee', required=False, dest='eevee_sqlite',
                     help="path to Eevee's Pokedex .sqlite file")
    parser.addoption('--showdown', required=False, dest='showdown_dir',
                     help="path to directory with Pokemon Showdown JSON files")


def pytest_collection_modifyitems(session, config, items):
    has_eevee = config.getoption('eevee_sqlite', None)
    has_showdown = config.getoption('showdown_dir', None)
    skip_eevee = pytest.mark.skip(reason="path to eevee pokedex sqlite not set; use --eevee option")
    skip_showdown = pytest.mark.skip(reason="path to Pokemon Showdown JSON files not set; use --showdown option")
    for item in items:
        if ('[eevee' in item.name and not has_eevee):
            item.add_marker(skip_eevee)
        if ('[showdown' in item.name and not has_showdown):
            item.add_marker(skip_showdown)


@pytest.fixture(scope="module",
                params=[(EeveeReader, 'eevee_sqlite'),
                        (ShowdownReader, 'showdown_dir')],
                ids=['eevee', 'showdown'])
def filled_pokedex(request):
    ReaderClass, option_name = request.param
    pokedex_path = request.config.getoption(option_name, None)
    reader = ReaderClass(pokedex_path)
    pokedex = PokedexStorage()
    reader.fill_pokedex(pokedex)

    with io.StringIO() as fh:
        pokedex._output_pokemon(fh)
        pokemon = json.loads(fh.getvalue())

    with io.StringIO() as fh:
        pokedex._output_moves(fh)
        moves = json.loads(fh.getvalue())

    with io.StringIO() as fh:
        pokedex._output_learnsets(fh)
        learnsets = json.loads(fh.getvalue())

    return {
        'pokedex': pokedex,
        'pokemon': pokemon,
        'moves': moves,
        'learnsets': learnsets
    }


