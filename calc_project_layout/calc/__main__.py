import click
from . import commands


@click.group()
def cli():
    pass


cli.add_command(commands.add)
cli.add_command(commands.subtract)
cli.add_command(commands.multiply)
cli.add_command(commands.divide)