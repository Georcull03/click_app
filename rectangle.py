import click


@click.command()
@click.option("--size", nargs=2, type=click.INT)
def cli(size):
    width, height = size
    click.echo(f"size: {size}")
    click.echo(f"{width} x {height}")
    click.echo(f"area = {width * height}^2")


if __name__ == "__main__":
    cli()
