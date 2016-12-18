
angular.module('pokemonTeamBuilder', [])
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
.service('PokemonMoves', ['$http', function($http) {
	this.moves = [];

	this.getMoves = function(pokemon_name) {
		var promise = $http.get('http://localhost:5000/pokemon/' + pokemon_name + '/moves');
		return promise;
	};
}])
.factory('PokemonTeam', ['PokemonList', function(PokemonList) {
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

	return {
		get: self.getTeam
	}
}])
.controller('PokemonTeamController', 
	['PokemonTeam', 'PokemonMoves', function(PokemonTeam, PokemonMoves) {
		var self = this;
		self.members = PokemonTeam.get();

		self.getMoves = function(member_object) {
			console.log(member_object);
			var pokemon_name = member_object.pokemon.id;
			PokemonMoves.getMoves(pokemon_name).then(function(pokemon_moves) {
				member_object.available_moves = pokemon_moves.data;
				member_object.moves = ["", "", "", ""];
			})
		}
}])
.controller('PokemonListController', ['PokemonList', function(PokemonList) {
	var self = this;

	PokemonList.getPokemonList().then(function(pokemon_list) {
		self.available_pokemon = pokemon_list;
	})
}])
