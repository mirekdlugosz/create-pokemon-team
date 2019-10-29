"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2018  Mirosław Zalewski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

import pokedexreader.storage
import pokedexreader.constants


def test_versions_in_constants():
    """Verify duplicated version names are exactly the same in
    both places they appear in.
    """
    in_constants = pokedexreader.constants.Constants.known_versions
    in_valid_list = pokedexreader.constants.Constants.available_pokemon.keys()
    for one, two in zip(in_constants, in_valid_list):
        assert one == two

    assert set(in_constants) == set(in_valid_list)
