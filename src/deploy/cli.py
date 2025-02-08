import click

@click.group()
def cli():
    """Deploy CLI - Open-Source AI Implementation Toolkit"""
    click.echo("Welcome to Deploy!")

@click.command()
def hello():
    """Print a Hello message"""
    click.echo("Hello, Deploy user!")

cli.add_command(hello)

if __name__ == "__main__":
    cli()
