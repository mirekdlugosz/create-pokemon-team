"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2019  Mirek Długosz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

import pytest

from pokedexreader.constants import Constants


def test_pokemon_with_many_forms(filled_pokedex):
    expected = {'diamond-pearl': ["deoxys", "deoxysattack", "deoxysdefense", "deoxysspeed",
                                  "wormadam", "wormadamsandy", "wormadamtrash", "giratina",
                                  "shaymin", "arceus", "arceusbug", "arceusdark", "arceusdragon",
                                  "arceuselectric", "arceusfighting", "arceusfire",
                                  "arceusflying", "arceusghost", "arceusgrass", "arceusground",
                                  "arceusice", "arceuspoison", "arceuspsychic", "arceusrock",
                                  "arceussteel", "arceuswater"],
                'platinum': ["giratina", "giratinaorigin", "shaymin", "shayminsky"],
                'black-white': ["kyurem", "meloetta", "meloettapirouette", "genesect",
                                "genesectdouse", "genesectshock", "genesectburn", "genesectchill"],
                'black-2-white-2': ["kyurem", "kyuremblack", "kyuremwhite"],
                'x-y': ["arceusfairy", "hoopa", "meowstic", "meowsticf"],
                'omega-ruby-alpha-sapphire': ["hoopa", "hoopaunbound"],
                'sun-moon': ["oricorio", "oricoriopompom", "oricoriopau", "oricoriosensu",
                             "lycanroc", "lycanrocmidnight", "silvally", "silvallybug",
                             "silvallydark", "silvallydragon", "silvallyelectric", "silvallyfairy",
                             "silvallyfighting", "silvallyfire", "silvallyflying", "silvallyghost",
                             "silvallygrass", "silvallyground", "silvallyice", "silvallypoison",
                             "silvallypsychic", "silvallyrock", "silvallysteel", "silvallywater",
                             "necrozma"],
                'ultra-sun-ultra-moon': ["lycanrocdusk", "necrozmaduskmane", "necrozmadawnwings",
                                         "necrozmaultra"]
                }
    for game, pokemon_list in expected.items():
        all_pokemon = [item['id'] for item in filled_pokedex['pokemon'][game]]
        assert all_pokemon
        for pokemon in pokemon_list:
            assert pokemon in all_pokemon
        assert all(pokemon in all_pokemon for pokemon in pokemon_list)


def test_ignored_pokemon_is_not_present(filled_pokedex):
    ignored_pokemon_list = ['pichu-spiky-eared', 'pikachu-rock-star', 'marowak-totem',
                            'castform-sunny', 'burmy-sandy', 'mothim-plant', 'cherrim-sunshine',
                            'shellos-west', 'gastrodon-east', 'arceus-unknown',
                            'basculin-red-striped', 'deerling-summer', 'sawsbuck-autumn',
                            'tornadus-incarnate', 'thundurus-therian', 'keldeo-ordinary',
                            'keldeo-resolute', 'greninja-battle-bond', 'greninja-ash',
                            'scatterbug-river', 'spewpa-polar', 'vivillon-fancy' 'flabebe-red',
                            'floette-yellow', 'floette-eternal', 'florges-blue', 'furfrou-star',
                            'aegislash-shield', 'aegislash-blade', 'pumpkaboo-small',
                            'gourgeist-large', 'xerneas-active', 'zygarde-10', 'zygarde-complete',
                            'minior-indigo-meteor', 'minior-meteor', 'minior-blue',
                            'mimikyu-busted', 'magearna-original']

    for game in filled_pokedex['pokemon']:
        pokemon_list = [item['id'] for item in filled_pokedex['pokemon'][game]]
        assert pokemon_list
        for ignored in ignored_pokemon_list:
            assert ignored not in pokemon_list


def test_order_in_pokedex(filled_pokedex):
    game = 'ultra-sun-ultra-moon'
    pokemon_list = [item['id'] for item in filled_pokedex['pokemon'][game]]
    assert pokemon_list.index('bulbasaur') == 0
    assert pokemon_list.index('bulbasaur') < pokemon_list.index('abra')
    assert pokemon_list.index('charmander') == pokemon_list.index('charmeleon') - 1
    assert pokemon_list.index('venusaur') == pokemon_list.index('venusaurmega') - 1
    assert pokemon_list.index('igglybuff') == pokemon_list.index('jigglypuff') - 1
    assert pokemon_list.index('rhyhorn') == pokemon_list.index('rhyperior') - 2
    assert pokemon_list.index('pikachu') == pokemon_list.index('raichualola') - 2
    assert pokemon_list.index('vulpixalola') == pokemon_list.index('ninetalesalola') - 2
    assert pokemon_list.index('mimejr') == pokemon_list.index('starmie') + 1


@pytest.mark.parametrize("pokemon_id,name", [
    ("beedrillmega", "Mega Beedrill"),
    ("charizardmegax", "Mega Charizard X"),
    ("kyogreprimal", "Kyogre (Primal Reversion)"),
    ("deoxys", "Deoxys (Normal Forme)"),
    ("wormadam", "Wormadam (Plant Cloak)"),
    ("wormadamsandy", "Wormadam (Sandy Cloak)"),
    ("rotomheat", "Heat Rotom"),
    ("giratina", "Giratina (Altered Forme)"),
    ("giratinaorigin", "Giratina (Origin Forme)"),
    ("shaymin", "Shaymin (Land Forme)"),
    ("shayminsky", "Shaymin (Sky Forme)"),
    ("arceusdark", "Arceus (Dark Type)"),
    ("darmanitan", "Darmanitan (Standard Mode)"),
    ("darmanitanzen", "Darmanitan (Zen Mode)"),
    ("kyuremwhite", "Kyurem (White)"),
    ("kyuremblack", "Kyurem (Black)"),
    ("meloetta", "Meloetta (Aria Forme)"),
    ("meloettapirouette", "Meloetta (Pirouette Forme)"),
    ("genesectburn", "Genesect (Burn Drive)"),
    ("meowstic", "Meowstic (Male)"),
    ("meowsticf", "Meowstic (Female)"),
    ("hoopa", "Hoopa (Confined)"),
    ("hoopaunbound", "Hoopa (Unbound)"),
    ("raichualola", "Alolan Raichu"),
    ("oricoriopau", "Oricorio (Pa’u Style)"),
    ("oricoriosensu", "Oricorio (Sensu Style)"),
    ("lycanroc", "Lycanroc (Midday Form)"),
    ("silvallyelectric", "Silvally (Electric Type)"),
    ("necrozmaduskmane", "Necrozma (Dusk Mane)"),
    ("necrozmadawnwings", "Necrozma (Dawn Wings)"),
    ("necrozmaultra", "Necrozma (Ultra)"),
    ("darmanitangalar", "Galarian Darmanitan (Standard Mode)"),
    ("darmanitangalarzen", "Galarian Darmanitan (Zen Mode)"),
    ("yamaskgalar", "Galarian Yamask"),
    ("indeedee", "Indeedee (Male)"),
    ("indeedeef", "Indeedee (Female)"),
    ("zamazentacrowned", "Crowned Zamazenta"),
])
def test_forme_name(filled_pokedex, pokemon_id, name):
    unavailable_in_eevee = ["darmanitangalar", "darmanitangalarzen", "yamaskgalar",
                            "indeedee", "indeedeef", "zamazentacrowned"]
    if filled_pokedex['reader'] == "EeveeReader" and pokemon_id in unavailable_in_eevee:
        pytest.skip(f"{pokemon_id} is not available in EeveeDex")

    in_any = False
    for game in filled_pokedex['pokemon']:
        pokemon = next((item for item in filled_pokedex['pokemon'][game]
                        if item['id'] == pokemon_id), None)
        if not pokemon:
            continue
        in_any = True
        assert pokemon['name'] == name
    assert in_any


@pytest.mark.parametrize("game,expected", [
    ("ruby-sapphire", ["deoxys"]),
    ("emerald", ["deoxysspeed"]),
    ("firered-leafgreen", ["deoxysattack", "deoxysdefense"]),
    ("x-y", ["deoxys", "deoxysattack", "deoxysdefense", "deoxysspeed"])
])
def test_deoxys_in_gen_3(filled_pokedex, game, expected):
    pokemon_list = [item['id'] for item in filled_pokedex['pokemon'][game]
                    if 'deoxys' in item['id']]
    assert pokemon_list == expected


def test_mega_in_gen_6(filled_pokedex):
    fake_mega = ['yanmega', 'meganium']

    reference_xy_mega = [pokemon for pokemon in Constants.available_pokemon['x-y']
                         if "mega" in pokemon and pokemon not in fake_mega]
    reference_oras_mega = [pokemon for pokemon in
                           Constants.available_pokemon['omega-ruby-alpha-sapphire']
                           if "mega" in pokemon and pokemon not in fake_mega]

    pokemon = filled_pokedex['pokemon']
    xy_mega_list = [item['id'] for item in pokemon['x-y']
                    if 'mega' in item['id'] and item['id'] not in fake_mega]
    oras_mega_list = [item['id'] for item in pokemon['omega-ruby-alpha-sapphire']
                      if 'mega' in item['id'] and item['id'] not in fake_mega]
    assert set(xy_mega_list) == set(reference_xy_mega)
    for oras_mega in set(reference_oras_mega) - set(reference_xy_mega):
        assert oras_mega not in xy_mega_list
    assert set(oras_mega_list) == set(reference_oras_mega)


@pytest.mark.parametrize("pokemon,last_game,type_,new_type", [
    ("azumarill", "black-2-white-2", ["Water"], ["Water", "Fairy"]),
    ("azurill", "black-2-white-2", ["Normal"], ["Normal", "Fairy"]),
    ("rotomheat", "heartgold-soulsilver", ["Electric", "Ghost"], ["Electric", "Fire"]),
    ("togekiss", "black-2-white-2", ["Normal", "Flying"], ["Fairy", "Flying"]),
    ("jigglypuff", "black-2-white-2", ["Normal"], ["Normal", "Fairy"])
])
def test_pokemon_type_before_change(filled_pokedex, pokemon, last_game, type_, new_type):
    versions = Constants.known_versions
    any_game = False
    for game in versions[:versions.index(last_game) + 1]:
        try:
            pokemon_obj = next(item for item in filled_pokedex['pokemon'][game]
                               if pokemon in item['id'])
        except (KeyError, StopIteration):
            continue
        any_game = True
        assert pokemon_obj['type'] == type_
    assert any_game

    game = versions[versions.index(last_game) + 1]
    pokemon_obj = next((item for item in filled_pokedex['pokemon'][game]
                       if pokemon in item['id']), None)
    assert pokemon_obj['type'] == new_type


def test_pokemon_in_learnsets(filled_pokedex):
    for version, pokemon_list in Constants.available_pokemon.items():
        if version not in filled_pokedex['learnsets']:
            continue
        assert len(filled_pokedex['learnsets'][version]) == len(pokemon_list)


def test_smeargle_moves(filled_pokedex):
    for learnset in filled_pokedex['learnsets'].values():
        try:
            smeargle_moves = learnset['smeargle']
        except KeyError:
            continue
        # there were 250 moves in gen II, when Smeargle was introduced
        assert len(smeargle_moves) > 250
        for move in Constants.invalid_smeargle_moves:
            assert move not in smeargle_moves


@pytest.mark.parametrize("pokemon_with,pokemon_without,moves,skip_games", [
    (['wormadam'], ['wormadamsandy', 'wormadamtrash'], ['razorleaf', 'growth', 'leafstorm'], []),
    (['wormadamsandy'], ['wormadam', 'wormadamtrash'], ['rockblast', 'harden', 'fissure'], []),
    (['wormadamtrash'], ['wormadam', 'wormadamsandy'], ['mirrorshot', 'metalsound', 'ironhead'], []),
    (['kyurem'], ['kyuremwhite', 'kyuremblack'], ['scaryface', 'glaciate'], ['sword-shield']),
    (['kyurem'], ['kyuremwhite', 'kyuremblack'], ['glaciate'], []),
    (['kyuremwhite'], ['kyurem', 'kyuremblack'], ['fusionflare', 'iceburn'], []),
    (['kyuremblack'], ['kyurem', 'kyuremwhite'], ['fusionbolt', 'freezeshock'], []),
    (['meowstic'], ['meowsticf'], ['charm', 'imprison', 'meanlook', 'miracleeye', 'mistyterrain', 'quickguard'],
     ['sword-shield']),
    (['meowstic'], ['meowsticf'], ['imprison', 'meanlook', 'mistyterrain', 'quickguard'], []),
    (['meowsticf'], ['meowstic'], ['extrasensory', 'futuresight', 'magicalleaf', 'mefirst', 'storedpower'],
     ['sword-shield']),
    (['meowsticf'], ['meowstic'], ['extrasensory', 'futuresight', 'magicalleaf', 'storedpower'], []),
    (['lycanrock', 'lycanrocdusk'], ['lycanrocmidnight'], ['accelerock'], []),
    (['lycanrocmidnight', 'lycanrocdusk'], ['lycanroc'], ['counter'], []),
    (['lycanroc'], ['lycanrocmidnight', 'lycanrocdusk'], ['quickattack'], ['sword-shield']),
    (['lycanroc', 'lycanrocdusk'], ['lycanrocmidnight'], ['quickattack'], ['sun-moon', 'ultra-sun-ultra-moon']),
])
def test_exclusive_form_moves(filled_pokedex, pokemon_with, pokemon_without, moves, skip_games):
    for game_name, game_learnset in filled_pokedex['learnsets'].items():
        if game_name in skip_games:
            continue
        if not all(pokemon in game_learnset for pokemon in pokemon_with + pokemon_without):
            continue
        for move in moves:
            know_list = [move in game_learnset[pokemon] for pokemon in pokemon_with]
            dont_know_list = [move not in game_learnset[pokemon] for pokemon in pokemon_without]
            assert all(know_list)
            assert all(dont_know_list)


@pytest.mark.parametrize("pokemon_list,moves", [
    (["deoxys", "deoxysattack", "deoxysdefense", "deoxysspeed"],
     ["superpower", "zapcannon", "amnesia", "counter", "irondefense", "mirrorcoat",
      "spikes", "agility", "extremespeed", "swift"]),
    (["giratina", "giratinaorigin"], ["painsplit", "magiccoat", "tailwind"]),
    (["shaymin", "shayminsky"], ["aromatherapy", "healingwish", "synthesis",
                                 "airslash", "leafstorm", "quickattack"]),
    (["hoopa", "hoopaunbound"], ["hyperspacefury", "knockoff", "hyperspacehole",
                                 "nastyplot", "phantomforce", "zenheadbutt"])
])
def test_changeable_form_moves(filled_pokedex, pokemon_list, moves):
    for game_learnset in filled_pokedex['learnsets'].values():
        if not all(pokemon in game_learnset for pokemon in pokemon_list):
            continue
        for move in moves:
            know_list = [move in game_learnset[pokemon] for pokemon in pokemon_list]
            # all Pokemon in group know the move, or none knows it
            assert sum(know_list) in (0, len(pokemon_list))


@pytest.mark.parametrize("prevo,pokemon,move", [
    ("bulbasaur", "venusaur", "seedbomb"),
    ("magby", "magmortar", "uproar"),
    ("minccino", "cinccino", "hypervoice"),
])
def test_prevolution_exclusive_moves(filled_pokedex, prevo, pokemon, move):
    for game_learnset in filled_pokedex['learnsets'].values():
        if not all(poke in game_learnset for poke in (prevo, pokemon)):
            continue
        know_list = [move in game_learnset[poke] for poke in (prevo, pokemon)]
        # all Pokemon in group know the move, or none knows it
        assert sum(know_list) != 1


@pytest.mark.parametrize("pokemon,move", [
    ("venusaurmega", "petaldance"),
    ("charizardmegax", "fireblast"),
    ("charizardmegay", "fireblast"),
])
def test_mega_evolution_moves(filled_pokedex, pokemon, move):
    for game in ['x-y', 'omega-ruby-alpha-sapphire', 'sun-moon', 'ultra-sun-ultra-moon']:
        assert move in filled_pokedex['learnsets'][game][pokemon]


@pytest.mark.parametrize("pokemon,move,game", [
    ("charizard", "blastburn", "firered-leafgreen"),
    ("beedrill", "bugbite", "heartgold-soulsilver"),
    ("marowak", "outrage", "black-2-white-2"),
    ("blastoise", "focuspunch", "omega-ruby-alpha-sapphire"),
    ("vikavolt", "snore", "ultra-sun-ultra-moon")
])
def test_tutor_moves(filled_pokedex, pokemon, move, game):
    assert move in filled_pokedex['learnsets'][game][pokemon]


@pytest.mark.parametrize("pokemon,move,game", [
    ("gengar", "icepunch", "emerald"),
    ("meganium", "frenzyplant", "diamond-pearl"),
    ("samurott", "hydrocannon", "black-white"),
    ("dragalge", "dracometeor", "x-y"),
    ("decidueye", "grasspledge", "sun-moon"),
])
def test_tutor_exceptional_moves(filled_pokedex, pokemon, move, game):
    assert move in filled_pokedex['learnsets'][game][pokemon]


@pytest.mark.parametrize("pokemon,move", [
    ("pidgeot", "substitute"),
    ("sandslash", "seismictoss"),
])
def test_tutor_gen_3(filled_pokedex, pokemon, move):
    for game in ['emerald', 'firered-leafgreen']:
        assert move in filled_pokedex['learnsets'][game][pokemon]


@pytest.mark.parametrize("pokemon,move", [
    ("jolteon", "magnetrise"),
    ("gardevoir", "signalbeam")
])
def test_tutor_gen_4(filled_pokedex, pokemon, move):
    for game in ['platinum', 'heartgold-soulsilver']:
        assert move in filled_pokedex['learnsets'][game][pokemon]


@pytest.mark.parametrize("game,has_fairy", [
    ("black-white", False),
    ("sun-moon", True)
])
def test_natural_gift_expansion(filled_pokedex, game, has_fairy):
    skip = ""
    if not has_fairy:
        skip = "Fairy"

    natural_gifts = [f"naturalgift{type_.lower()}" for type_
                     in Constants.types if type_ != skip]
    moves = filled_pokedex['learnsets'][game]['lugia']
    assert all(gift in moves for gift in natural_gifts)

    assert ("naturalgiftfairy" in moves) == has_fairy


def test_hidden_power_expansion(filled_pokedex):
    hidden_powers = [f"hiddenpower{type_.lower()}" for type_
                     in Constants.types if type_ not in ["Normal", "Fairy"]]
    moves = filled_pokedex['learnsets']['ultra-sun-ultra-moon']['araquanid']
    assert all(power in moves for power in hidden_powers)


def test_move_type_depending_on_pokemon(filled_pokedex):
    moves = [move_obj for move_name, move_obj in filled_pokedex['moves'].items()
             if move_name in Constants.moves_inheriting_type]
    assert all("uses_pokemon_type" in move for move in moves)


def test_move_that_doesnt_change_type(filled_pokedex):
    moves = [move_obj for move_name, move_obj in filled_pokedex['moves'].items()
             if move_name not in Constants.moves_inheriting_type]
    assert all("uses_pokemon_type" not in move for move in moves)


def test_moves_that_changed_type(filled_pokedex):
    moves = [move_obj for move_name, move_obj in filled_pokedex['moves'].items()
             if move_name in Constants.move_type_overrides.keys()]
    assert all("override" in move for move in moves)


def test_moves_that_didnt_change_type(filled_pokedex):
    moves = [move_obj for move_name, move_obj in filled_pokedex['moves'].items()
             if move_name not in Constants.move_type_overrides.keys()]
    assert all("override" not in move for move in moves)
