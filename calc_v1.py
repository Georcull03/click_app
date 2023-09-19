import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def add(a, b):
    click.echo(f"{a} + {b} = {a + b}")


if __name__ == "__main__":
    cli()
