
angular.module('pokemonTeamBuilder', ['ui.select', 'ngSanitize'])
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
	this.type_effectiveness = {
		"Normal": {
			"Normal": 1,
			"Fire": 1,
			"Water": 1,
			"Electric": 1,
			"Grass": 1,
			"Ice": 1,
			"Fighting": 1,
			"Poison": 1,
			"Ground": 1,
			"Flying": 1,
			"Psychic": 1,
			"Bug": 1,
			"Rock": 0.5,
			"Ghost": 0,
			"Dragon": 1,
			"Dark": 1,
			"Steel": 0.5,
			"Fairy": 1
		},
		"Fire": {
			"Normal": 1,
			"Fire": 0.5,
			"Water": 0.5,
			"Electric": 1,
			"Grass": 2,
			"Ice": 2,
			"Fighting": 1,
			"Poison": 1,
			"Ground": 1,
			"Flying": 1,
			"Psychic": 1,
			"Bug": 2,
			"Rock": 0.5,
			"Ghost": 1,
			"Dragon": 0.5,
			"Dark": 1,
			"Steel": 2,
			"Fairy": 1
		},
		"Water":  {
			"Normal": 1,
			"Fire": 2,
			"Water": 0.5,
			"Electric": 1,
			"Grass": 0.5,
			"Ice": 1,
			"Fighting": 1,
			"Poison": 1,
			"Ground": 2,
			"Flying": 1,
			"Psychic": 1,
			"Bug": 1,
			"Rock": 2,
			"Ghost": 1,
			"Dragon": 0.5,
			"Dark": 1,
			"Steel": 1,
			"Fairy": 1
		},
		"Electric":  {
			"Normal": 1,
			"Fire": 1,
			"Water": 2,
			"Electric": 0.5,
			"Grass": 0.5,
			"Ice": 1,
			"Fighting": 1,
			"Poison": 1,
			"Ground": 0,
			"Flying": 2,
			"Psychic": 1,
			"Bug": 1,
			"Rock": 1,
			"Ghost": 1,
			"Dragon": 0.5,
			"Dark": 1,
			"Steel": 1,
			"Fairy": 1
		},
		"Grass":  {
			"Normal": 1,
			"Fire": 0.5,
			"Water": 2,
			"Electric": 1,
			"Grass": 0.5,
			"Ice": 1,
			"Fighting": 1,
			"Poison": 0.5,
			"Ground": 2,
			"Flying": 0.5,
			"Psychic": 1,
			"Bug": 0.5,
			"Rock": 2,
			"Ghost": 1,
			"Dragon": 0.5,
			"Dark": 1,
			"Steel": 0.5,
			"Fairy": 1
		},
		"Ice": {
			"Normal": 1,
			"Fire": 0.5,
			"Water": 0.5,
			"Electric": 1,
			"Grass": 2,
			"Ice": 0.5,
			"Fighting": 1,
			"Poison": 1,
			"Ground": 2,
			"Flying": 2,
			"Psychic": 1,
			"Bug": 1,
			"Rock": 1,
			"Ghost": 1,
			"Dragon": 2,
			"Dark": 1,
			"Steel": 0.5,
			"Fairy": 1
		},
		"Fighting": {
			"Normal": 2,
			"Fire": 1,
			"Water": 1,
			"Electric": 1,
			"Grass": 1,
			"Ice": 2,
			"Fighting": 1,
			"Poison": 0.5,
			"Ground": 1,
			"Flying": 0.5,
			"Psychic": 0.5,
			"Bug": 0.5,
			"Rock": 2,
			"Ghost": 0,
			"Dragon": 1,
			"Dark": 2,
			"Steel": 2,
			"Fairy": 0.5
		},
		"Poison": {
			"Normal": 1,
			"Fire": 1,
			"Water": 1,
			"Electric": 1,
			"Grass": 2,
			"Ice": 1,
			"Fighting": 1,
			"Poison": 0.5,
			"Ground": 0.5,
			"Flying": 1,
			"Psychic": 1,
			"Bug": 1,
			"Rock": 0.5,
			"Ghost": 0.5,
			"Dragon": 1,
			"Dark": 1,
			"Steel": 0,
			"Fairy": 2
		},
		"Ground": {
			"Normal": 1,
			"Fire": 2,
			"Water": 1,
			"Electric": 2,
			"Grass": 0.5,
			"Ice": 1,
			"Fighting": 1,
			"Poison": 2,
			"Ground": 1,
			"Flying": 0,
			"Psychic": 1,
			"Bug": 0.5,
			"Rock": 2,
			"Ghost": 1,
			"Dragon": 1,
			"Dark": 1,
			"Steel": 2,
			"Fairy": 1
		},
		"Flying": {
			"Normal": 1,
			"Fire": 1,
			"Water": 1,
			"Electric": 0.5,
			"Grass": 2,
			"Ice": 1,
			"Fighting": 2,
			"Poison": 1,
			"Ground": 1,
			"Flying": 1,
			"Psychic": 1,
			"Bug": 2,
			"Rock": 0.5,
			"Ghost": 1,
			"Dragon": 1,
			"Dark": 1,
			"Steel": 0.5,
			"Fairy": 1
		},
		"Psychic": {
			"Normal": 1,
			"Fire": 1,
			"Water": 1,
			"Electric": 1,
			"Grass": 1,
			"Ice": 1,
			"Fighting": 2,
			"Poison": 2,
			"Ground": 1,
			"Flying": 1,
			"Psychic": 0.5,
			"Bug": 1,
			"Rock": 1,
			"Ghost": 1,
			"Dragon": 1,
			"Dark": 0,
			"Steel": 0.5,
			"Fairy": 1
		},
		"Bug": {
			"Normal": 1,
			"Fire": 0.5,
			"Water": 1,
			"Electric": 1,
			"Grass": 2,
			"Ice": 1,
			"Fighting": 0.5,
			"Poison": 0.5,
			"Ground": 1,
			"Flying": 0.5,
			"Psychic": 2,
			"Bug": 1,
			"Rock": 1,
			"Ghost": 0.5,
			"Dragon": 1,
			"Dark": 2,
			"Steel": 0.5,
			"Fairy": 0.5
		},
		"Rock": {
			"Normal": 1,
			"Fire": 2,
			"Water": 1,
			"Electric": 1,
			"Grass": 1,
			"Ice": 2,
			"Fighting": 0.5,
			"Poison": 1,
			"Ground": 0.5,
			"Flying": 2,
			"Psychic": 1,
			"Bug": 2,
			"Rock": 1,
			"Ghost": 1,
			"Dragon": 1,
			"Dark": 1,
			"Steel": 0.5,
			"Fairy": 1
		},
		"Ghost": {
			"Normal": 0,
			"Fire": 1,
			"Water": 1,
			"Electric": 1,
			"Grass": 1,
			"Ice": 1,
			"Fighting": 1,
			"Poison": 1,
			"Ground": 1,
			"Flying": 1,
			"Psychic": 2,
			"Bug": 1,
			"Rock": 1,
			"Ghost": 2,
			"Dragon": 1,
			"Dark": 0.5,
			"Steel": 1,
			"Fairy": 1
		},
		"Dragon": {
			"Normal": 1,
			"Fire": 1,
			"Water": 1,
			"Electric": 1,
			"Grass": 1,
			"Ice": 1,
			"Fighting": 1,
			"Poison": 1,
			"Ground": 1,
			"Flying": 1,
			"Psychic": 1,
			"Bug": 1,
			"Rock": 1,
			"Ghost": 1,
			"Dragon": 2,
			"Dark": 1,
			"Steel": 0.5,
			"Fairy": 0
		},
		"Dark": {
			"Normal": 1,
			"Fire": 1,
			"Water": 1,
			"Electric": 1,
			"Grass": 1,
			"Ice": 1,
			"Fighting": 0.5,
			"Poison": 1,
			"Ground": 1,
			"Flying": 1,
			"Psychic": 2,
			"Bug": 1,
			"Rock": 1,
			"Ghost": 2,
			"Dragon": 1,
			"Dark": 0.5,
			"Steel": 1,
			"Fairy": 0.5
		},
		"Steel": {
			"Normal": 1,
			"Fire": 0.5,
			"Water": 0.5,
			"Electric": 0.5,
			"Grass": 1,
			"Ice": 2,
			"Fighting": 1,
			"Poison": 1,
			"Ground": 1,
			"Flying": 1,
			"Psychic": 1,
			"Bug": 1,
			"Rock": 2,
			"Ghost": 1,
			"Dragon": 1,
			"Dark": 1,
			"Steel": 0.5,
			"Fairy": 2
		},
		"Fairy": {
			"Normal": 1,
			"Fire": 0.5,
			"Water": 1,
			"Electric": 1,
			"Grass": 1,
			"Ice": 1,
			"Fighting": 2,
			"Poison": 0.5,
			"Ground": 1,
			"Flying": 1,
			"Psychic": 1,
			"Bug": 1,
			"Rock": 1,
			"Ghost": 1,
			"Dragon": 2,
			"Dark": 2,
			"Steel": 0.5,
			"Fairy": 1
		}
		}

	//Array(19).join("1").split("").map(Number) - tworzy 18 jedynek
	this.default_type_effectiveness = {
		"Normal": 1,
		"Fire": 1,
		"Water": 1,
		"Electric": 1,
		"Grass": 1,
		"Ice": 1,
		"Fighting": 1,
		"Poison": 1,
		"Ground": 1,
		"Flying": 1,
		"Psychic": 1,
		"Bug": 1,
		"Rock": 1,
		"Ghost": 1,
		"Dragon": 1,
		"Dark": 1,
		"Steel": 1,
		"Fairy": 1
	}

	this.damage_multiplier = function(attacking_type, defending_type) {
		return this.type_effectiveness[attacking_type][defending_type];
	}

	this.effect_table = function(defending_typing) {
		var self = this;
		console.log(defending_typing);
		var result = angular.copy(self.default_type_effectiveness);
		if (typeof(defending_typing) !== "undefined") {
			for (var i = 0; i < defending_typing.length; i++) {
				Object.keys(result).forEach(function(attack_type) {
					result[attack_type] = result[attack_type] * self.damage_multiplier(attack_type, defending_typing[i])
				})
			}
		}
		return Object.values(result);
	}
	
	this.attackTypeTemplate = [
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	]

	this.computeTypeEffectivenessForPokemon = function(pokemon) {
		var self = this;
		console.log(pokemon);
		var defenses = self.effect_table(pokemon.pokemon.type);
		var moves = pokemon.moves.filter(function(move) {
			return ! (move == "" || move.category === 'status');
		})
		var attacks = angular.copy(self.attackTypeTemplate);
		moves.forEach(function(move) {
			Object.keys(self.default_type_effectiveness).forEach(function(defending_type, type_index) {
				var effect = self.damage_multiplier(move.type, defending_type);
				var effect_index = 2;
				if (effect > 1) {
					effect_index = 0;
				} else if (effect < 1) {
					effect_index = 1
				}
				attacks[effect_index][type_index] += 1;
			})
		})
		return [defenses].concat(attacks);
	}

	this.computeTypeEffectivenessTable = function(team) {
		var self = this;
		var typeEffectivenessTable = []
		team.forEach(function(teamMember) {
			var rows = self.computeTypeEffectivenessForPokemon(teamMember);
			typeEffectivenessTable = typeEffectivenessTable.concat(rows)
		})
		typeEffectivenessTable = typeEffectivenessTable[0].map(function(col, i) { 
			return typeEffectivenessTable.map(function(row) {
				return row[i];
			})
		});
		return typeEffectivenessTable;
	}

	this.computeTypeCoverageTable = function(team) {
		return;
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
		getTeamMembers: self.getTeam,
		getTypeEffectivenessTable: self.getTypeEffectivenessTable,
		getTypeCoverageTable: self.getTypeCoverageTable
	}
}])
.controller('PokemonTeamController', 
	['PokemonTeam', 'PokemonMoves', function(PokemonTeam, PokemonMoves) {
		var self = this;
		// TODO: Unnecessary duplication
		self.typeTable = [ "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy" ];
		self.header_cells = ["Type",
			"Effect", "SE", "NVE", "NE",
			"Effect", "SE", "NVE", "NE",
			"Effect", "SE", "NVE", "NE",
			"Effect", "SE", "NVE", "NE",
			"Effect", "SE", "NVE", "NE",
			"Effect", "SE", "NVE", "NE"
		]
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
