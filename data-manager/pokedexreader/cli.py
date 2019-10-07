"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2018  Mirosław Zalewski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""

import argparse
import pathlib

from .storage import PokedexStorage
from .readers import EeveeReader, ShowdownReader


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--eevee', required=False, dest='eevee_sqlite',
                        help="path to Eevee's Pokedex .sqlite file")
    parser.add_argument('--showdown', required=False, dest='showdown_dir',
                        help="path to directory with Pokemon Showdown JSON files")
    parser.add_argument('--dump', action='append',
                        choices=['pokemon', 'learnsets', 'moves', 'all'],
                        help="dump data from Pokedex, don't write any files")
    parser.add_argument('--pretty', action='store_true',
                        help="pretty-print results (affects --dump only)")
    parser.add_argument('-o', '--output-dir',
                        help="write files to OUTPUT_DIR. \"-\" means STDOUT")
    return parser.parse_args()


def cli():
    args = parse_arguments()

    if not any([args.eevee_sqlite, args.showdown_dir]):
        msg = ("One of --eevee or --showdown is mandatory and"
               " must point at existing file/directory")
        raise SystemExit(msg)

    if args.eevee_sqlite and not pathlib.Path(args.eevee_sqlite).is_file():
        msg = f"{args.eevee_sqlite} does not exist"
        raise SystemExit(msg)

    if args.showdown_dir and not pathlib.Path(args.showdown_dir).is_dir():
        msg = f"{args.showdown_dir} does not exist"
        raise SystemExit(msg)

    pokedex = PokedexStorage()

    if args.eevee_sqlite:
        eeveedex = EeveeReader(args.eevee_sqlite)
        eeveedex.fill_pokedex(pokedex)

    if args.showdown_dir:
        showdowndex = ShowdownReader(args.showdown_dir)
        showdowndex.fill_pokedex(pokedex)

    if args.dump:
        pokedex.dump_data(args.dump, args.pretty)

    if args.output_dir:
        pokedex.output(args.output_dir)


if __name__ == '__main__':
    cli()
