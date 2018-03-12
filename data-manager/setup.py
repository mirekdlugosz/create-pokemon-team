#!/usr/bin/env python3

from setuptools import setup


setup(
    name='pokedexreader',
    version='0.1',
    description='Helper script for backend',
    author='Mirosław Zalewski',
    author_email='mz@miroslaw-zalewski.eu',
    entry_points={
        'console_scripts': ['pokedexreader=pokedexreader.cli:cli'],
    },
    include_package_data=True,
    license='GPLv3',
)
