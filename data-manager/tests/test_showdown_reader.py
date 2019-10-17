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

from pokedexreader.storage import PokedexStorage

"""
to check:
- pokemon
    - ignored ones are not present
    - special ones are present (forms differing in some significant property)
    - order inside pokedex
    - name (Arceus, pokemon with different forms)
    - presence in special game-pokemon configurations (deoxys in gen 3, mega in gen 6)
    - type before it changed (e.g. Jigglypuff prior to gen 6)
- moves
    - smeargle
    - pokemon that can change form any time with form-exclusive move (for all form-exclusive moves, verify every form has it)
    - move that can be learned by prevolution only
    - mega evolution (can it learn everything that prior evolution could)
    - tutor - properly recognize only last game in generation has it
    - tutor - exception - first game in generation (starter moves)
    - tutor - exception - two games in generation (gen III and IV only)
    - natural gift expansion
    - hidden power expansion
    - every move that changes type depending on Pokemon type
    - type before it changed (e.g. Bite in gen I?)
"""


@pytest.fixture(scope="module")
def filled_showdowndex(showdown):
    pokedex = PokedexStorage()
    showdown.fill_pokedex(pokedex)

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


def test_pokemon_with_many_forms(filled_showdowndex):
    pass


def test_ignored_pokemon_is_not_present(filled_showdowndex):
    pass


def test_order_in_pokedex(filled_showdowndex):
    pass


def test_arceus_name(filled_showdowndex):
    pass


def test_deoxys_in_gen_3(filled_showdowndex):
    pass


def test_mega_in_gen_6(filled_showdowndex):
    pass


def test_pokemon_fairy_type_before_gen_6(filled_showdowndex):
    pass


def test_smeargle_moves(filled_showdowndex):
    pass


def test_changeable_form_moves(filled_showdowndex):
    pass


def test_prevolution_exclusive_moves(filled_showdowndex):
    pass


def test_mega_evolution_moves(filled_showdowndex):
    pass


def test_tutor_moves(filled_showdowndex):
    pass


def test_tutor_exceptional_moves(filled_showdowndex):
    pass


def test_tutor_gen_3(filled_showdowndex):
    pass


def test_natural_gift_expansion(filled_showdowndex):
    pass


def test_hidden_power_expansion(filled_showdowndex):
    pass


def test_move_type_depending_on_pokemon(filled_showdowndex):
    pass


def test_moves_with_changed_type(filled_showdowndex):
    pass
