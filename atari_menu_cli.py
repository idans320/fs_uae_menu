#!/usr/bin/env python3
import click
from atari_menu.cmd import generateDb
from click_default_group import DefaultGroup
from atari_menu.app import main

@click.group(cls=DefaultGroup,default="init", default_if_no_args=True)
def cli():
    pass

@cli.command()
@click.option("--game_directory","-p", required=True, help="Path of the atari collection")
def generate_db(game_directory):
    generateDb.run(game_directory)

@cli.command()
def init():
    main()

if __name__ == '__main__':
    cli()