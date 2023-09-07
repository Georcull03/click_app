import click


@click.command()
@click.option(
    "--weekday",
    type=click.Choice(
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ],
        # Line can be used to allow value if written in different case
        # case_sensitive=False,
    ),
)
def cli(weekday):
    click.echo(f"Weekday: {weekday}")


if __name__ == "__main__":
    cli()
