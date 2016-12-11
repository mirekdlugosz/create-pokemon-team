
angular.module('pokemonTeamBuilder', [])
	.factory('PokemonList', ['$http', function($http) {
		var self = this;
		self.pokemon = [];

		self.getPokemon = function() {
			var promise = $http.get('http://localhost:5000/pokemon').then(function(response) {
				self.pokemon = response.data;
				return self.pokemon;
			}, function(errResponse) {
				console.error('Error downloading Pokemon list');
			});
			return promise;
		}

		return {
			getPokemon: self.getPokemon
		}
	}])
	.service('PokemonMoves', ['$http', function($http) {
		this.moves = [];

		this.getMoves = function(pokemon_name) {
			var promise = $http.get('http://localhost:5000/pokemon/' + pokemon_name + '/moves');
			return promise;
		};
	}])
	.controller('PokemonListCtrl', ['PokemonList', function(pokemonList) {
		var self = this;
		pokemonList.getPokemon().then(function(pokemon_list) {
			self.pokemon = pokemon_list;
		})
	}])
	.controller('PokemonMovesCtrl', ['PokemonMoves', function(PokemonMoves) {
		var self = this;
		self.moves = [];

		self.getMoves = function() {
			PokemonMoves.getMoves(self.pokemon).then(function(pokemon_moves) {
				self.moves = pokemon_moves.data;
			})
		}

	}])
