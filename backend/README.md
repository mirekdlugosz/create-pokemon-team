# createPokémon.team backend

Flask application that provides data through REST service.

## Requirements

* Python 3.4 or later
* [Flask](http://flask.pocoo.org/)
* JSON files created by `data-reader` component

## Installation

Create new virtual environment and install dependencies from requirements.txt file in root of repository:

```
$ python3 -m venv /path/to/venv
$ . /path/to/venv/bin/activate
$ pip install -r ../requirements.txt
```

Then, use `pokedexreader` command to create JSON data files:

```
$ pokedexreader <options> -o backend/api/data/
```

You can - and should! - use one virtual environment for both `backend` and `data-manager`.

## Usage

When virtual environment for this project is active, run:

```
./run.py
```

REST service will be available at `http://127.0.0.1:8861/`.

## Running tests

When virtual environment for this project is active, run:

```
pytest
```

## License

Licensed under GNU Affero General Public License (GNU AGPL) Version 3 or later.
See `LICENSE` file in root of this repository for details.
