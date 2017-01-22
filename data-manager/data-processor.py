#!/usr/bin/env python3

import os
import json
# we might need it later on
# print(os.path.dirname(os.path.realpath(__file__)))

# # Read data from source JSON files

with open("data-source/learnsets-sumo.json") as fh:
    learnsets = json.load(fh)
    learnsets = learnsets["data"]

with open("data-source/moves-sumo.json") as fh:
    movedex = json.load(fh)
    movedex = movedex["data"]

with open("data-source/pokedex-sumo.json") as fh:
    pokedex = json.load(fh)
    pokedex = pokedex["data"]

# # Helper global variables
known_types = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting",
	"Fire", "Flying", "Ghost", "Grass", "Ground", "Ice",
	"Normal", "Poison", "Psychic", "Rock", "Steel", "Water"]
hidden_power_list = ["hiddenpower" + move_type.lower() for move_type in known_types if move_type not in ["Normal", "Fairy"]]
natural_gift_list = ["naturalgift" + move_type.lower() for move_type in known_types]
genesect_types = {
        "Burn": "Fire",
        "Chill": "Ice",
        "Douse": "Water",
        "Shock": "Electric",
        }

# # Helper functions

def is_alola(pokemon):
    if "forme" in pokemon and pokemon["forme"] == "Alola":
        return True
    return False

# # Data fixes

# ## Eternal Flower Floette was never distributed
# ## Vivillon Fancy and Pokeball do not differ from standard Vivillon in any way
for pokemon in ["floetteeternalflower", "vivillonfancy", "vivillonpokeball"]:
    del(pokedex[pokemon])

# ## Wishiwashi has both "forme" and "baseSpecies", fooling us into thinking it
#    is different forme of some species; there is one entry in database, though

del(pokedex["wishiwashi"]["forme"])
del(pokedex["wishiwashi"]["baseSpecies"])

# ## Flabebe line does not have `baseSpecies` key set up, preventing us from
#    making connection between different flower colors and base forme
for pokemon in ["flabebe", "floette", "florges"]:
    for color in ["blue", "orange", "white", "yellow"]:
        pokemon_to_fix = "{}{}".format(pokemon, color)
        pokedex[pokemon_to_fix]["baseSpecies"] = pokemon.title()

# ## Nidoran has sex in species name
pokedex["nidoranf"]["species"] = "Nidoran (Female)"
pokedex["nidoranm"]["species"] = "Nidoran (Male)"

# ## Everyone could learn Natural Gift in gen 4
#    We usually don't differentiate how move could be learned,
#    but Natural Gift has variable type and leaving it gives 
#    false impression about Pokemon type coverage

for pokemon_id in learnsets:
    learnset = learnsets[pokemon_id]["learnset"]
    if "naturalgift" in learnset and learnset["naturalgift"] == ['4M']:
        del(learnset["naturalgift"])

for move_type in known_types:
    movedex["naturalgift{}".format(move_type.lower())] = {
            "name": "Natural Gift ({})".format(move_type),
            "type": move_type,
            "category": "Physical",
            }

# # Create basic data structure for further processing

known_pokemon = list(pokedex)
processed_pokemon = {}

while known_pokemon:
    for pokemon_id in known_pokemon:
        pokemon = pokedex[pokemon_id]
        moves = set()
        related = None

        if "prevo" in pokemon:
            related = pokemon["prevo"]

        if "baseSpecies" in pokemon and not is_alola(pokemon):
            related = pokemon["baseSpecies"].lower()

        if related:
            if related in processed_pokemon:
                moves.update(processed_pokemon[related]["moveset"])
            else:
                continue

        pokemon_name = pokemon["species"]
        if "forme" in pokemon:
            base_species = pokemon["baseSpecies"]
            forme = pokemon["forme"]

            pokemon_name = "{} ({})".format(base_species, forme)

            if any([string in pokemon["species"] for string in ["Mega", "Primal", "Rotom", "Ash", "Midnight"]]):
                pokemon_name = "{} {}".format(forme, base_species)

                if "-" in forme:
                    pokemon_name = "Mega {} {}".format(base_species, forme[-1])

            if pokemon_id.endswith("alola"):
                pokemon_name = "Alolan {}".format(base_species)

            if pokemon["species"].endswith(("Hoopa-Unbound", "Giratina-Origin")):
                pokemon_name = "{} {}".format(base_species, forme)

            if pokemon["species"] == "Meowstic-F":
                pokemon_name = "Meowstic (Female)"

            if base_species == "Oricorio":
                pokemon_name = "{} ({} style)".format(base_species, forme)

            if base_species == "Wormadam":
                pokemon_name = "{} ({} cloak)".format(base_species, forme)

        if pokemon_id in learnsets:
            moves.update(set(learnsets[pokemon_id]["learnset"]))

        pokemon_data = {
                "id": pokemon_id,
                "name": pokemon_name,
                "type": pokemon["types"],
                "moveset": moves,
                "num": pokemon["num"],
                "species": pokemon["species"],
                }
        processed_pokemon[pokemon_id] = pokemon_data
        known_pokemon.remove(pokemon_id)

# Create final Pokemon list and save it to file

pokemon_list = []

for pokemon_id in sorted(processed_pokemon, key=lambda pokemon: (processed_pokemon[pokemon]["num"], processed_pokemon[pokemon]["species"])):
    pokemon = processed_pokemon[pokemon_id]
    pokemon_list.append({
        "id": pokemon["id"],
        "name": pokemon["name"],
        "type": pokemon["type"],
        })

with open("../backend/api/pokemon-list.json", "w") as fh:
    json.dump(pokemon_list, fh)

# # Save moves data in pokemon-specific JSON file

for pokemon_id in processed_pokemon:
    pokemon = processed_pokemon[pokemon_id]

    if "hiddenpower" in pokemon["moveset"]:
        pokemon["moveset"].update(hidden_power_list)
        pokemon["moveset"].remove("hiddenpower")

    if "naturalgift" in pokemon["moveset"]:
        pokemon["moveset"].update(natural_gift_list)
        pokemon["moveset"].remove("naturalgift")

    if pokemon_id == "smeargle":
        for move in movedex:
            if "isZ" in movedex[move]:
                continue
            if move in ["hiddenpower", "naturalgift"]:
                continue
            pokemon["moveset"].update([move])

    moveset = []
    for move_id in pokemon["moveset"]:
        move = movedex[move_id]
        move_name = move["name"]
        move_type = move["type"]

        if move_id in ["judgment", "multiattack"]:
            move_name = "{} ({})".format(move["name"], pokemon["type"][0])
            move_type = pokemon["type"][0]

        if move_id == "technoblast" and pokemon_id not in ["genesect", "smeargle"]:
            move_type = genesect_types[ pokemon["species"].split("-")[1] ]

        if move_id == "revelationdance":
            move_type = pokemon["type"][0]

        moveset.append({
            "name": move_name,
            "type": move_type,
            "category": move["category"],
            })

    moveset = sorted(moveset, key=lambda move: move["name"])

    with open("../backend/api/moves/"+ pokemon_id+".json", 'w') as fh:
        json.dump(moveset, fh)
