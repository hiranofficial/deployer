import click
from deploy.logger import get_logger

# Initialize the logger
logger = get_logger()

@click.group()
def cli():
    """Deploy CLI - Open-Source AI Implementation Toolkit"""
    logger.info("Deploy CLI initialized.")

@click.command()
def hello():
    """Print a Hello message"""
    logger.info("Hello, Deploy user!")

cli.add_command(hello)

if __name__ == "__main__":
    cli()
