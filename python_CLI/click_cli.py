import click


@click.command()
@click.option('--count', default=1, help='Number of greeting...')
@click.option('--name', prompt="Your name", help="This person to greeting")
def hello_world(count, name):
    for x in range(count):
        click.echo(f"Hello {name}")


@click.group()
def cli():
    pass


@click.command()
def initDb():
    click.echo("Initial database")


@click.command()
@click.option('--drop', type=str, help="Drop database_name")
def dropDB(drop):
    click.echo(f"Dropped db {drop}")


cli.add_command(initDb)
cli.add_command(dropDB)

