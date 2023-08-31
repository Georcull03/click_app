import click


@click.command("hello")
@click.version_option("0.1.0", prog_name="hello")
def hello():
    click.echo("Hello, you are using the Python Click module!")


if __name__ == "__main__":
    hello()
