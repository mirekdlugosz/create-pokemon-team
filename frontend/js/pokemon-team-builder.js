
angular.module('pokemonTeamBuilder', ['ui.select', 'ngSanitize', 'ui.bootstrap'])
.factory('PokemonList', ['$http', function($http) {
	var self = this;
	self.pokemon = [];

	self.getPokemonList = function() {
		var promise = $http.get('http://localhost:5000/pokemon').then(function(response) {
			self.pokemon = response.data;
			return self.pokemon;
		}, function(errResponse) {
			console.error('Error downloading Pokemon list');
		});
		return promise;
	}

	return {
		getPokemonList: self.getPokemonList
	}
}])
.service('TypeTable', [function() {
	var transposeArray = function(array) {
		return array[0].map(function(col, i) { 
			return array.map(function(row) {
				return row[i];
			})
		});
	}

	var arrayOfNumbers = function(number, length) {
		return Array(length+1).join(number.toString()).split("").map(Number)
	}

	/* Note:
	 * Because working with annotated (labeled) multi-dimensional data structures
	 * in JavaScript is extremely awkward, we resort to using simple 2-D array.
	 * `type_effectiveness` array must have exactly the same number of elements as
	 * `type_names` array; the same holds for each array inside `type_effectiveness`.
	 * Order of elements must be retained in both arrays
	 */
	var type_names = [
		"Normal", "Fire", "Water", "Electric", "Grass", "Ice", 
		"Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug",
		"Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
	]

	var type_effectiveness = [
		[  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,0.5,  0,  1,  1,0.5,  1],
		[  1,0.5,0.5,  1,  2,  2,  1,  1,  1,  1,  1,  2,0.5,  1,0.5,  1,  2,  1],
		[  1,  2,0.5,  1,0.5,  1,  1,  1,  2,  1,  1,  1,  2,  1,0.5,  1,  1,  1],
		[  1,  1,  2,0.5,0.5,  1,  1,  1,  0,  2,  1,  1,  1,  1,0.5,  1,  1,  1],
		[  1,0.5,  2,  1,0.5,  1,  1,0.5,  2,0.5,  1,0.5,  2,  1,0.5,  1,0.5,  1],
		[  1,0.5,0.5,  1,  2,0.5,  1,  1,  2,  2,  1,  1,  1,  1,  2,  1,0.5,  1],
		[  2,  1,  1,  1,  1,  2,  1,0.5,  1,0.5,0.5,0.5,  2,  0,  1,  2,  2,0.5],
		[  1,  1,  1,  1,  2,  1,  1,0.5,0.5,  1,  1,  1,0.5,0.5,  1,  1,  0,  2],
		[  1,  2,  1,  2,0.5,  1,  1,  2,  1,  0,  1,0.5,  2,  1,  1,  1,  2,  1],
		[  1,  1,  1,0.5,  2,  1,  2,  1,  1,  1,  1,  2,0.5,  1,  1,  1,0.5,  1],
		[  1,  1,  1,  1,  1,  1,  2,  2,  1,  1,0.5,  1,  1,  1,  1,  0,0.5,  1],
		[  1,0.5,  1,  1,  2,  1,0.5,0.5,  1,0.5,  2,  1,  1,0.5,  1,  2,0.5,0.5],
		[  1,  2,  1,  1,  1,  2,0.5,  1,0.5,  2,  1,  2,  1,  1,  1,  1,0.5,  1],
		[  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,  1,  2,  1,0.5,  1,  1],
		[  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,0.5,  0],
		[  1,  1,  1,  1,  1,  1,0.5,  1,  1,  1,  2,  1,  1,  2,  1,0.5,  1,0.5],
		[  1,0.5,0.5,0.5,  1,  2,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1,0.5,  2],
		[  1,0.5,  1,  1,  1,  1,  2,0.5,  1,  1,  1,  1,  1,  1,  2,  2,0.5,  1]
	]

	var typeNameToIndex = function(type_name) {
		return type_names.indexOf(type_name);
	}

	var typeIndexToName = function(type_index) {
		return type_names[type_index];
	}

	var attackEffectByIndex = function(attacking_type, defending_type) {
		return type_effectiveness[attacking_type][defending_type];
	}

	var attackEffectByName = function(attacking_type, defending_type) {
		return attackEffectByIndex(typeNameToIndex(attacking_type), typeNameToIndex(defending_type));
	}

	/* FIXME: This should be general function that can handle
	 * single index, single string, array of indices and array of strings
	 * as input value, preferably for both `attacking_type` and `defending_type`.
	 * But we always know what we are working with, so we may call
	 * lower-level functions if effect by indices/single strings 
	 * are needed
	*/ 
	var attackEffect = function(attacking_type, defending_type_array) {
		var result = 1;
		defending_type_array.forEach(function(defending_type) {
			result *= attackEffectByName(attacking_type, defending_type)
		})
		return result;
	}

	var computeDefenseEffectivenessTable = function(defending_typing) {
		var result = arrayOfNumbers(1, type_names.length);
		if (typeof(defending_typing) !== "undefined") {
			type_names.forEach(function(attacking_type, attacking_type_index) {
				result[attacking_type_index] = attackEffect(attacking_type, defending_typing);
			})
		}
		return result;
	}

	var computeTypeEffectivenessForPokemon = function(pokemon) {
		var self = this;
		var attacksEffectivenessTable = [
			arrayOfNumbers(0, type_names.length),
			arrayOfNumbers(0, type_names.length),
			arrayOfNumbers(0, type_names.length)
		]

		var defenseEffectivenessTable = computeDefenseEffectivenessTable(pokemon.pokemon.type);
		var moves = pokemon.moves.filter(function(move) {
			return ! (move == "" || move.category === 'status');
		})
		type_names.forEach(function(defending_type, defending_type_index) {
			moves.forEach(function(move) {
				var effect = attackEffectByName(move.type, defending_type);
				var effect_index = 2;
				if (effect > 1) {
					effect_index = 0;
				} else if (effect < 1) {
					effect_index = 1
				}
				attacksEffectivenessTable[effect_index][defending_type_index] += 1;
			})
		})
		return [ defenseEffectivenessTable ].concat(attacksEffectivenessTable);
	}

	this.computeTypeEffectivenessTable = function(team) {
		var self = this;
		var typeEffectivenessTable = []
		team.forEach(function(teamMember) {
			var rows = computeTypeEffectivenessForPokemon(teamMember);
			typeEffectivenessTable = typeEffectivenessTable.concat(rows)
		})
		return transposeArray(typeEffectivenessTable);
	}

	this.computeTypeCoverageTable = function(team) {
		var type_coverage_table = [
			arrayOfNumbers(0, type_names.length),
			arrayOfNumbers(0, type_names.length),
			arrayOfNumbers(0, type_names.length),
			arrayOfNumbers(0, type_names.length),
			arrayOfNumbers(0, type_names.length)
		]
		team = team.filter(function(pokemon) {
			return pokemon.pokemon != "";
		})
		type_names.forEach(function(type, type_index) {
			team.forEach(function(pokemon) {
				var effect = attackEffect(type, pokemon.pokemon.type);
				if (effect > 1) {
					type_coverage_table[0][type_index] += 1;
				} else if (effect < 1) {
					type_coverage_table[1][type_index] += 1;
				}
				var moves = pokemon.moves.filter(function(move) {
					return ! (move == "" || move.category === 'status');
				})
				moves.forEach(function(move) {
					var effect = attackEffectByName(move.type, type);
					var effect_index = 4;
					if (effect < 1) {
						effect_index = 3;
					} else if (effect > 1) {
						effect_index = 2;
					}
					type_coverage_table[effect_index][type_index] += 1;
				})
			})
		})
		return transposeArray(type_coverage_table);
	}

	this.getTypeList = function() {
		return type_names;
	}
}])
.service('PokemonMoves', ['$http', function($http) {
	// TODO: create cache, so selecting one Poke back and forth does not generate new requests
	this.moves = [];

	this.getMoves = function(pokemon_name) {
		var promise = $http.get('http://localhost:5000/pokemon/' + pokemon_name + '/moves');
		return promise;
	};
}])
.factory('PokemonTeam', ['TypeTable', 'PokemonList', function(TypeTable, PokemonList) {
	var self = this;
	self.team = [
		{
			pokemon: "",
			moves: ["", "", "", ""],
		},
		{
			pokemon: "",
			moves: ["", "", "", ""],
		},
		{
			pokemon: "",
			moves: ["", "", "", ""],
		},
		{
			pokemon: "",
			moves: ["", "", "", ""],
		},
		{
			pokemon: "",
			moves: ["", "", "", ""],
		},
		{
			pokemon: "",
			moves: ["", "", "", ""],
		}
	];

	self.getTypeList = function() {
		return TypeTable.getTypeList();
	}
	self.getTeam = function() {
		return self.team;
	}

	self.getTypeEffectivenessTable = function() {
		return TypeTable.computeTypeEffectivenessTable(self.team);
	}

	self.getTypeCoverageTable = function() {
		return TypeTable.computeTypeCoverageTable(self.team);
	}

	return {
		getTypeList: self.getTypeList,
		getTeamMembers: self.getTeam,
		getTypeEffectivenessTable: self.getTypeEffectivenessTable,
		getTypeCoverageTable: self.getTypeCoverageTable
	}
}])
.controller('PokemonTeamController', 
	['PokemonTeam', 'PokemonMoves', function(PokemonTeam, PokemonMoves) {
		var self = this;
		self.type_list = PokemonTeam.getTypeList();

		self.type_effectiveness_table_header = [
			{label: 'Effect', title: ''},
			{label: 'SE', title: 'Number of Super Effective moves'},
			{label: 'NVE', title: 'Number of Not Very Effective moves'},
			{label: 'NE', title: 'Number of moves with neutral effectiveness'}
		];
		self.type_effectiveness_table_header = [ "Effect", "SE", "NVE", "NE" ];

		self.members = PokemonTeam.getTeamMembers();

		self.getMoves = function(member_object) {
			var pokemon_name = member_object.pokemon.id;
			PokemonMoves.getMoves(pokemon_name).then(function(pokemon_moves) {
				member_object.available_moves = pokemon_moves.data;
				member_object.moves = ["", "", "", ""];
			})
			self.updateTables();
		}

		self.updateTables = function() {
			self.typeEffectivenessTable = PokemonTeam.getTypeEffectivenessTable();
			self.typeCoverageTable = PokemonTeam.getTypeCoverageTable();
		}

		self.updateTables();

}])
.controller('PokemonListController', ['PokemonList', function(PokemonList) {
	var self = this;

	PokemonList.getPokemonList().then(function(pokemon_list) {
		self.available_pokemon = pokemon_list;
	})
}])
