# createPokémon.team backend

Flask application that provides data through REST service.

## Requirements

* Python 3.4 or later
* [Flask](http://flask.pocoo.org/)
* json module (should come with Python)
* [pipenv](https://github.com/pypa/pipenv) for installation
* JSON files created by data-reader component

## Installation

Run following command:

```
pipenv install --dev
```

## Usage

When running in virtualenv shell (`pipenv shell`), run:

```
./run.py
```

REST service will be available at `http://127.0.0.1:8861/`.

## Running tests

When running in virtualenv shell (`pipenv shell`), run:

```
pytest
```

## License

Licensed under GNU Affero General Public License (GNU AGPL) Version 3 or later.
See `LICENSE` file in root of this repository for details.
