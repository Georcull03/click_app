import click


@click.command()
@click.option("--size", type=(click.INT, click.INT))
def cli(size):
    width, height = size
    click.echo(f"size: {size}")
    click.echo(f"{width} x {height}")
    click.echo(f"area: {width * height}cm^2")


if __name__ == "__main__":
    cli()