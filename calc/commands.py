import click


@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def add(a, b):
    """Adds two floats"""
    click.echo(f"{a} + {b} = {a + b}")


@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def subtract(a, b):
    """Subtracts two floats"""
    click.echo(f"{a} - {b} = {a - b}")


@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def multiply(a, b):
    """Multiplies two floats"""
    click.echo(f"{a} * {b} = {a * b}")


@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def divide(a, b):
    """Divides two floats"""
    click.echo(f"{a} / {b} = {a / b}")
