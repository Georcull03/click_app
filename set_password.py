import click


@click.command()
@click.option("--name", prompt="Username")
@click.password_option("--set-password", prompt="Password")
def cli(name, set_password):
    # change password
    click.echo("Password successfully changed!")
    click.echo(f"Username: {name}")
    click.echo(f"Password: {set_password}")


if __name__ == "__main__":
    cli()
