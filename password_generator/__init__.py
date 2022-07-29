import click
from .generation import generate_password
from config import Config
from vault import VaultManager

@click.group()
def cli(): pass


@cli.command()
@click.option('--save', default=False, is_flag=True, help="Save your password into your vault | DEFAULT=False")
@click.option('--length', default=8, help="Determine the length of the password | DEFAULT=8")
@click.option('--upper', default=True, help="Enable/Disable uppercase chars (ABC) | DEFAULT=True")
@click.option('--lower', default=True, help="Enable/Disable lowercase chars (abc) | DEFAULT=True")
@click.option('--numeric', default=True, help="Enable/Disable numeric chars (123) | Default=True")
@click.option('--punct', default=True, help="Enable/Disable punctuation chars (@!?) | Default=True")
def generate(save, length, upper, lower, numeric, punct):
    """Generate a Strong Password"""

    if save:
        while True:
            password = generate_password(length, numeric, lower, upper, punct)
            if click.confirm(f"[{password}] OK?"):
                click.echo("Password has been saved!")
                break 
            
        


@cli.command()
@click.option("--vault", default="default", help="Pick a vault to put your password in (business, social_media, etc.)")
@click.argument("password_identifier")
def save(vault, password_identifier):
    """Save your passwords into your vaults"""
    # TODO: Check if the given vault exists here.
    vault_password = click.prompt(f"Enter your vault password for your vault {vault}", hide_input=True)
    password = click.prompt("Enter your password", hide_input=True)
    password_repetition = click.prompt("Enter your password again", hide_input=True)
    
    # The following lines of codes are in test/debug purpose
    if password == password_repetition:
        # TODO: Save the password to the given vault or default vault.
        click.echo("Password has been saved!")
        click.echo(f"You've written {vault_password} for your vault password unlocking your vault")
        click.echo(f"{password} is your password")
        click.echo(f"{password_identifier} is your password_identifier")
    else:
        click.echo("Please make sure you did write the same passwords")


def main():
    conf = Config()
    vault = VaultManager(conf)
    cli()


if __name__ == "__main__":
    main()
