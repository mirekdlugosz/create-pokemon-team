# createPokémon.team data-manager

data-manager takes data from specified source and outputs JSON files readable by backend.

## Requirements

* Python 3.4 or later
* sqlite3 and json modules (should come with Python)
* [pipenv](https://github.com/pypa/pipenv) for installation
* SQLite file with data from [veekun Pokédex](https://github.com/veekun/pokedex)

## Installation

Run following command:

```
pipenv install --dev
```

## Setting up data source

This component requires some data source. Currently only SQLite file with veekun Pokédex is supported. You can acquire it by running following commands:

```
git clone https://github.com/veekun/pokedex.git
cd pokedex
pipenv --two install -e .
pipenv shell
python setup.py install
pokedex load
```

Path to SQLite file will be printed out at the beginning of output. Or you can use `pokedex status`.

## Usage

When running in virtualenv shell (`pipenv shell`), run:

```
pokedexreader --eevee <path_to_veekun_pokedex.sqlite> -o <path_to_backend/api/data/>
```

See `pokedexreader --help` for all available options.

## Data sources

There are three publicly-availble sources of data about Pokémon:

* [veekun Pokédex](https://veekun.com/dex)
* [Pokémon Showdown!](https://pokemonshowdown.com/)
* [Bulbapedia](https://bulbapedia.bulbagarden.net/)

Unfortunately, each comes with their own limitations and drawbacks.

veekun uses custom scripts to dump data from game files. While it is very comprehensive, it is also completely oblivious to event moves. Being one-man show means that it is rather slow to update once new games are released. veekun stores data in bunch of CSV files that are loaded into SQL database.

Pokémon Showdown! is online battle simulator. It completely omits generations I and II, as battle mechanics was revamped in generation III. It stores data in couple of JavaScript files - they can be easily converted to JSON, but require something that can understand JS.

Bulbapedia is wiki dedicated to Pokémon. They are probably the most comprehensive and quickest to update, but their database is not publicly availble and they actively fight all attempts at mass scraping of data. Even if they would not, a lot of interesting data seems to not be structured in any particular way, making it extremely hard to read automatically.

At the moment, **this script supports only veekun SQLite file as data source**.

## License

Licensed under GNU Affero General Public License (GNU AGPL) Version 3 or later.
See `LICENSE` file in root of this repository for details.
