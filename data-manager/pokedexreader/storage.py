class PokedexStorage():
    def __init__(self):
        self.pokemon = {}        # dictionary of available Pokemon
        self.pokemon_moves = {}  # Pokemon move learnsets
        self.moves = {}          # move information
        self._types = set(["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                           "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug",
                           "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"])

    def add_pokemon(self, generation=None, pokemon_id=None, name=None, pokemon_type=None):
        if not generation:
            raise ValueError('Generation cannot be empty')

        if not pokemon_id:
            raise ValueError('Pokemon ID cannot be empty')

        if not name:
            raise ValueError('Pokemon name cannot be empty')

        if not pokemon_type:
            raise ValueError('Pokemon Type cannot be empty')

        if set(pokemon_type) & self._types != set(pokemon_type):
            raise ValueError('Unknown Type in {}; must be one of {}'.format(pokemon_type, self._types))

        pokemon_struct = {
            "id": pokemon_id,
            "name": name,
            "type": pokemon_type
        }

        self.pokemon.setdefault(generation, []).append(pokemon_struct)

    def dump_data(self, data_to_dump):
        if 'all' in data_to_dump:
            data_to_dump.extend(['pokemon', 'learnsets', 'moves'])
        if 'pokemon' in data_to_dump:
            print(self.pokemon)
        if 'learnsets' in data_to_dump:
            print(self.pokemon_moves)
        if 'moves' in data_to_dump:
            print(self.moves)
