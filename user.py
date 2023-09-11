import click


def read_username():
    return "admin"


def read_password():
    return "secret"


@click.command()
@click.option("--name", prompt="Username")
@click.option("--password", prompt="Password", hide_input=True)
def cli(name, password):
    if name != read_username() or password != read_password():
        click.echo("Invalid user credentials")
    else:
        click.echo(f"User {name} successfully logged in!")


if __name__ == "__main__":
    cli()