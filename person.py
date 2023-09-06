import click


@click.command()
@click.option("--profile", type=click.Tuple([str, int, str]))
def cli(profile):
    click.echo(f"Hello {profile[0]}! You are {profile[1]} years old! You are from {profile[2]}")


if __name__ == "__main__":
    cli()