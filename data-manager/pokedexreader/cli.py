import argparse
import sys
import os

from .storage import PokedexStorage
from .readers import EeveeReader


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--eevee', required=True, dest='eevee_sqlite',
                        help="path to Eevee's Pokedex .sqlite file")
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

    if not os.path.isfile(args.eevee_sqlite):
        print("{} does not exist".format(args.eevee_sqlite))
        sys.exit(1)

    pokedex = PokedexStorage()
    eeveedex = EeveeReader(args.eevee_sqlite)
    eeveedex.fill_pokedex(pokedex)

    if args.dump:
        pokedex.dump_data(args.dump, args.pretty)

    if args.output_dir:
        pokedex.output(args.output_dir)


if __name__ == '__main__':
    cli()
