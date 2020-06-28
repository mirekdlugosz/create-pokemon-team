# createPokémon.team data-manager

data-manager takes data from specified source and outputs JSON files readable by backend.

## Requirements

* Python 3.6 or later
* Node.js 12.0 or later (optional, only if Pokemon Showdown is used as data source)
* At least one data source:
    * SQLite file with data from [veekun Pokédex](https://github.com/veekun/pokedex)
    * Copy of [Pokemon Showdown repository](https://github.com/Zarel/Pokemon-Showdown)

## Installation

Create new virtual environment and install dependencies from requirements.txt file in root of repository:

```
$ python3 -m venv /path/to/venv
$ . /path/to/venv/bin/activate
$ pip install -r ../requirements.txt
```

You can - and should! - use one virtual environment for both `backend` and `data-manager`.

## Setting up data source

This component requires some data source. Currently SQLite file with veekun Pokédex and `data` directory from Pokemon Showdown repository are supported.

### veekun SQLite file

You can acquire veekun SQLite by running following commands; make sure to run them outside of **this** project repository:

```
git clone https://github.com/veekun/pokedex.git
cd pokedex
pipenv --two install -e .
pipenv shell
python setup.py install
pokedex load
```

Path to SQLite file will be printed out at the beginning of output. Or you can use `pokedex status`.

### Pokemon Showdown `data` directory

Acquire copy of Pokemon Showdown repository. You need to build the project to use files in `data` directory. Compiled files are designed to be used by Node.js and they must be transformed to JSON first.

First, run these commands outside of **this** project repository:

```
# run these commands outside of this project repository
git clone https://github.com/smogon/pokemon-showdown.git
cd pokemon-showdown
npm install
npm run build
```

Second, run below command in this project repository; remember to adjust paths:

```
node create-pokemon-team/data-manager/showdown2json pokemon-showdown/.data-dist/ /tmp/showdown-data-json/
```

## Usage

When virtual environment for this project is active, run:

```
pokedexreader --eevee <path_to_veekun_pokedex.sqlite> --showdown <path_to_showdown_data_json_dir> -o <path_to_backend/api/data/>
```

One of `--eevee` and `--showdown` can be omitted. For best results, use both of them.

See `pokedexreader --help` for all available options.

## Data sources

There are three publicly-available sources of data about Pokémon:

* [veekun Pokédex](https://veekun.com/dex)
* [Pokémon Showdown!](https://pokemonshowdown.com/)
* [Bulbapedia](https://bulbapedia.bulbagarden.net/)

Unfortunately, each comes with their own limitations and drawbacks.

veekun uses custom scripts to dump data from game files. While it is very comprehensive, it is also completely oblivious to event moves. Being one-man show means that it is rather slow to update once new games are released. veekun stores data in bunch of CSV files that are loaded into SQL database.

Pokémon Showdown! is online battle simulator. It completely omits generations I and II, as battle mechanics was revamped in generation III. It stores data in couple of JavaScript files - they can be easily converted to JSON, but require something that can understand JS.

Bulbapedia is wiki dedicated to Pokémon. They are probably the most comprehensive and quickest to update, but their database is not publicly available and they actively fight all attempts at mass scraping of data. Even if they would not, a lot of interesting data seems to not be structured in any particular way, making it extremely hard to read automatically.

At the moment, **this script supports veekun SQLite file and Pokémon Showdown `data` directory as data sources**.

## License

Licensed under GNU Affero General Public License (GNU AGPL) Version 3 or later.
See `LICENSE` file in root of this repository for details.
