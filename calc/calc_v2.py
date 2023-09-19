import click
import commands


@click.group()
def cli():
    pass


cli.add_command(commands.add)
cli.add_command(commands.subtract)
cli.add_command(commands.multiply)
cli.add_command(commands.divide)

if __name__ == "__main__":
    cli()
