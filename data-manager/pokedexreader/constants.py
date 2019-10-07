"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2018  Mirosław Zalewski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

from .constants_pokedex import available_pokemon


class Constants():
    # Known types. Should be self-explanatory
    types = set(["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug",
                "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"])

    # Known versions. Usually two entries per generation.
    known_versions = [
        "red-blue", "yellow", "gold-silver", "crystal", "ruby-sapphire",
        "emerald", "firered-leafgreen", "diamond-pearl", "platinum",
        "heartgold-soulsilver", "black-white", "black-2-white-2", "x-y",
        "omega-ruby-alpha-sapphire", "sun-moon", "ultra-sun-ultra-moon",
    ]

    games_in_generation = (
        # empty item at index 0 to allow index == generation number
        (),
        # gen 1 - red/blue, yellow
        (known_versions[0], known_versions[1]),
        # gen 2 - gold/silver, crystal
        (known_versions[2], known_versions[3]),
        # gen 3 - ruby/sapphire, emerald, fire red/leaf green
        (known_versions[4], known_versions[5], known_versions[6]),
        # gen 4 - diamond/pearl, platinum, heart gold/soul silver
        (known_versions[7], known_versions[8], known_versions[9]),
        # gen 5 - black/white, black2/white2
        (known_versions[10], known_versions[11]),
        # gen 6 - x/y, omega ruby/alpha sapphire
        (known_versions[12], known_versions[13]),
        # gen 7 - sun/moon, ultra sun/ultra moon
        (known_versions[14], known_versions[15]),
    )

    # In the history of franchise, some Pokemon changed their type.
    # This dict contains ids of these Pokemon, their *previous* type
    # and id of version in which that type was *last used* (so version
    # is inclusive).
    # So far there were no Pokemon that changed type twice
    pokemon_type_overrides = {
        "azumarill": {
            "type": ['Water'],
            "last_version": "black-2-white-2",
        },
        "azurill": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "clefable": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "clefairy": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "cleffa": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "cottonee": {
            "type": ['Grass'],
            "last_version": "black-2-white-2",
        },
        "gardevoir": {
            "type": ['Psychic'],
            "last_version": "black-2-white-2",
        },
        "granbull": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "igglybuff": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "jigglypuff": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "kirlia": {
            "type": ['Psychic'],
            "last_version": "black-2-white-2",
        },
        "magnemite": {
            "type": ['Electric'],
            "last_version": "yellow",
        },
        "magneton": {
            "type": ['Electric'],
            "last_version": "yellow",
        },
        "marill": {
            "type": ['Water'],
            "last_version": "black-2-white-2",
        },
        "mawile": {
            "type": ['Steel'],
            "last_version": "black-2-white-2",
        },
        "mime-jr": {
            "type": ['Psychic'],
            "last_version": "black-2-white-2",
        },
        "mr-mime": {
            "type": ['Psychic'],
            "last_version": "black-2-white-2",
        },
        "ralts": {
            "type": ['Psychic'],
            "last_version": "black-2-white-2",
        },
        "rotom": {
            "type": ['Electric', 'Ghost'],
            "last_version": "heartgold-soulsilver",
        },
        "rotom-heat": {
            "type": ['Electric', 'Ghost'],
            "last_version": "heartgold-soulsilver",
        },
        "rotom-wash": {
            "type": ['Electric', 'Ghost'],
            "last_version": "heartgold-soulsilver",
        },
        "rotom-frost": {
            "type": ['Electric', 'Ghost'],
            "last_version": "heartgold-soulsilver",
        },
        "rotom-fan": {
            "type": ['Electric', 'Ghost'],
            "last_version": "heartgold-soulsilver",
        },
        "rotom-mow": {
            "type": ['Electric', 'Ghost'],
            "last_version": "heartgold-soulsilver",
        },
        "snubbull": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "togekiss": {
            "type": ['Normal', 'Flying'],
            "last_version": "black-2-white-2",
        },
        "togepi": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "togetic": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
        "whimsicott": {
            "type": ['Grass'],
            "last_version": "black-2-white-2",
        },
        "wigglytuff": {
            "type": ['Normal'],
            "last_version": "black-2-white-2",
        },
    }

    # In the history of franchise, some moves changed their type.
    # This dict contains ids of these moves, their *previous* type
    # and id of version in which that type was *last used* (so version
    # is inclusive).
    # So far there were no move that changed type twice
    # Curse and "???" (Unknown) type are deliberately left out
    move_type_overrides = {
        "bite": {
            "type": 'Normal',
            "last_version": 'yellow',
        },
        "gust": {
            "type": 'Normal',
            "last_version": 'yellow',
        },
        "karate-chop": {
            "type": 'Normal',
            "last_version": 'yellow',
        },
        "sand-attack": {
            "type": 'Normal',
            "last_version": 'yellow',
        },
        "charm": {
            "type": 'Normal',
            "last_version": "black-2-white-2",
        },
        "moonlight": {
            "type": 'Normal',
            "last_version": "black-2-white-2",
        },
        "sweet-kiss": {
            "type": 'Normal',
            "last_version": "black-2-white-2",
        },
    }

    # List of moves that change their type depending on type of Pokemon
    # that use them.
    moves_inheriting_type = [
        "judgment", "multi-attack", "revelation-dance"
    ]

    # Map of Pokemon available in each game
    available_pokemon = available_pokemon

    # List of Pokemon that were not available in given version despite
    # being introduced in previous one.
    invalid_pokemon_version = {
        "ruby-sapphire": ["deoxys-attack", "deoxys-defense", "deoxys-speed"],
        "firered-leafgreen": ["deoxys-normal", "deoxys-speed"],
        "emerald": ["deoxys-normal", "deoxys-attack", "deoxys-defense"],
    }

    # Used in Eevee Pokedex reader.
    # Some Pokemon have multiple forms that differ in a way that is not
    # relevant for us (e.g. by stats). This list is used to ensure
    # that all forms are treated as one
    eeveedex_equivalent_pokemon_ids = [
        "aegislash", "basculin", "burmy", "castform", "cherrim",
        "deerling", "flabebe", "floette", "florges", "furfrou",
        "gastrodon", "gourgeist", "keldeo", "landorus", "magearna",
        "mimikyu", "minior", "mothim", "pumpkaboo", "sawsbuck",
        "scatterbug", "shellos", "spewpa", "thundurus", "tornadus",
        "unown", "vivillon", "wishiwashi", "xerneas", "zygarde",
    ]

    # Used in Eevee Pokedex reader.
    # Few Pokemon have learnset differences in forms, but can change form
    # at will and do not forget moves learned while in different form.
    # This list allows us to get moves of form that has not yet been processed
    # in main loop.
    # This is the only place where we are forced to use numeric id.
    # Note that ids are casted as strings
    eeveedex_equivalent_movesets = [
        # Deoxys
        ["386", "10001", "10002", "10003"],
        # Giratina
        ["487", "10007"],
        # Shaymin
        ["492", "10006"],
        # Hoopa
        ["720", "10086"],
    ]

    # Used in Eevee Pokedex reader.
    # Previous evolution id refers to Pokemon species, but some
    # species can have multiple forms and evolution lines run along
    # forms, not across them. In other words, normal Sandshrew can
    # evolve only into normal Sandslash and Alolan Sandshrew can
    # evolve only into Alolan Sandslash.
    # As of generation VII, only Alola forms are affected by that
    eeveedex_evolves_from_override = {
        "raticate-alola": "rattata-alola",
        "sandslash-alola": "sandshrew-alola",
        "ninetales-alola": "vulpix-alola",
        "dugtrio-alola": "diglett-alola",
        "persian-alola": "meowth-alola",
        "graveler-alola": "geodude-alola",
        "golem-alola": "graveler-alola",
        "muk-alola": "grimer-alola",
    }

    # Used in Eevee Pokedex reader.
    # There are few moves in database that seemingly no Pokemon can
    # learn. This is most likely data dump artifact.
    # We specify manually what Pokemon in what version could
    # legitimately learn these moves.
    # Except for Zygarde, these moves are event-exclusive.
    # There are many event-exclusive moves that are left out of this dict.
    eeveedex_missing_moves = {
        "victini": {
            "black-white": ["v-create"],
            "black-2-white-2": ["v-create"],
            "x-y": ["v-create"],
            "omega-ruby-alpha-sapphire": ["v-create"],
            "sun-moon": ["v-create"],
        },
        "celebi": {
            "x-y": ["hold-back"],
        },
        "zygarde": {
            "sun-moon": ["thousand-arrows", "thousand-waves"],
            "ultra-sun-ultra-moon": ["thousand-arrows", "thousand-waves"],
        }
    }

    # Used in Eevee Pokedex reader.
    # SQL queries used to retrieve data from Eevee Pokedex.
    # Should be self-explanatory
    eeveedex_query_fetch_all_pokemon = """
        SELECT
        pokemon.identifier as pokemon_id,
        pokemon.id as pokemon_numeric_id,
        pokemon_forms.identifier as pokemon_form_identifier,
        pokemon_forms.form_identifier as pokemon_form_form_identifier,
        pokemon_form_names.pokemon_name as pokemon_form_pokemon_name,
        pokemon_form_names.form_name as pokemon_form_name,
        version_groups.identifier as pokemon_form_introduced_in_version,
        pokemon_species.id as pokemon_species_id,
        pokemon_species_names.name as pokemon_species_name,
        pokemon_species.evolves_from_species_id as pokemon_evolves_from
        FROM pokemon
        JOIN pokemon_forms ON pokemon_forms.pokemon_id = pokemon.id
        LEFT JOIN pokemon_form_names ON pokemon_form_names.pokemon_form_id = pokemon_forms.id
        LEFT JOIN languages as form_lang ON form_lang.id = pokemon_form_names.local_language_id
        JOIN pokemon_species ON pokemon.species_id = pokemon_species.id
        JOIN pokemon_species_names ON pokemon_species.id = pokemon_species_names.pokemon_species_id
        JOIN languages as specie_lang ON specie_lang.id = pokemon_species_names.local_language_id
        JOIN version_groups ON version_groups.id = pokemon_forms.introduced_in_version_group_id
        WHERE (form_lang.identifier IS NULL OR form_lang.identifier = 'en')
        AND (specie_lang.identifier IS NULL OR specie_lang.identifier = 'en')
        ORDER BY pokemon."order" ASC
    """
    eeveedex_query_fetch_all_moves = """
        SELECT
        moves.identifier as move_identifier,
        types.identifier as type,
        move_damage_classes.identifier as category,
        move_names.name as move_name
        FROM moves
        JOIN types ON types.id = moves.type_id
        JOIN move_damage_classes ON move_damage_classes.id = moves.damage_class_id
        JOIN move_names ON move_names.move_id = moves.id
        WHERE move_names.local_language_id = 9
        AND type != 'shadow'
        AND moves.pp != 1
    """
    eeveedex_query_fetch_all_moves_with_version = """
        SELECT
        version_groups.identifier as version,
        moves.identifier as move_id
        FROM versions
        JOIN version_groups ON version_groups.id = versions.version_group_id
        JOIN generations ON version_groups.generation_id = generations.id
        JOIN moves ON moves.generation_id = generations.id
        WHERE moves.pp != 1
        AND version_groups.identifier NOT IN ('colosseum', 'xd')
        GROUP BY version, move_id
        ORDER BY version_groups.id ASC, move_id ASC
    """
    # do note that this query is pseudo-parameterized (as passing list
    # as parameter is seemingly impossible)
    eeveedex_query_fetch_pokemon_moves = """
        SELECT
        version_groups.identifier as version,
        moves.identifier as move_id
        FROM pokemon
        JOIN pokemon_moves ON pokemon_moves.pokemon_id = pokemon.id
        JOIN moves ON moves.id = pokemon_moves.move_id
        JOIN version_groups ON version_groups.id = pokemon_moves.version_group_id
        WHERE pokemon.id IN ({})
        AND version_groups.identifier NOT IN ('colosseum', 'xd')
        GROUP BY version, move_id
        ORDER BY pokemon_moves.version_group_id ASC, move_id ASC
    """
    # this query is pseudo-parameterized for consistency
    eeveedex_query_fetch_pokemon_types = """
        SELECT
        type_names.name
        FROM pokemon_types
        JOIN type_names ON type_names.type_id = pokemon_types.type_id
        WHERE type_names.local_language_id = 9
        AND pokemon_types.pokemon_id = {}
        ORDER BY pokemon_types.slot ASC
    """
