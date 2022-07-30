import click
from .generation import generate_password
from .config import Config, VaultManager, CONFIG_FILE

WARNING_MESSAGE = \
    f"""
WARNING: YOU WON'T BE ABLE TO ACCESS YOUR VAULT WITHOUT THIS PASSWORD.
Notice: You'll need the salt value to access this vault in another system.
Don't forget to copy {CONFIG_FILE} file.
    """

config = Config()
vaultmanager = VaultManager(config)


@click.group()
def cli(): pass


@cli.command()
@click.option('--save', default=False, is_flag=True, help="Save your password into your vault | DEFAULT=False")
@click.option('--length', default=8, help="Determine the length of the password | DEFAULT=8")
@click.option('--upper/--no-upper', default=True, help="Enable/Disable uppercase chars (ABC) | DEFAULT=True")
@click.option('--lower/--no-lower', default=True, help="Enable/Disable lowercase chars (abc) | DEFAULT=True")
@click.option('--numeric/--no-numeric', default=True, help="Enable/Disable numeric chars (123) | Default=True")
@click.option('--punct/--no-punct', default=True, help="Enable/Disable punctuation chars (@!?) | Default=True")
def generate(save, length, upper, lower, numeric, punct):
    """Generate a Strong Password"""

    if save:
        while True:
            password = generate_password(length, numeric, lower, upper, punct)
            if click.confirm(f"[{password}] OK?"):
                click.echo("Password has been saved!")
                break
    else:
        password = generate_password(length, numeric, lower, upper, punct)
        click.echo(password)


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


@cli.group()
def vault():
    """Manages your vaults"""


@vault.command()
@click.argument("path", type=click.Path(exists=True))
def add(path):
    """Adds your existing vault into the config"""

    vault_name = click.prompt("Enter a name for this vault")
    is_default = click.confirm(f"Set {vault_name} as a default vault?")

    if is_default:
        click.echo(f"{vault_name} saved as default!")
        vaultmanager.default_vault = path
    else:
        click.echo("Done!")


@vault.command()
@click.argument("vault_name")
@click.argument("path", required=False, type=click.Path(exists=True))
def create(vault_name, path):
    """Creates a new vault"""

    click.echo("Creating a new vault...")
    while True:
        password = click.prompt("Enter a strong password for your vault", hide_input=True)
        repetition = click.prompt("Repeat your password", hide_input=True)
        if password == repetition:
            click.echo(WARNING_MESSAGE)
            if path:
                click.echo(f"Vault Path: {path}")
            is_default = click.confirm(f"Set {vault_name} as your default vault?")
            click.echo("Done!")
            if is_default:
                vaultmanager.default_vault = path 
            break


def main():
    cli()

if __name__ == "__main__":
    
    main()
