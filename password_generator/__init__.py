import click
from .generation import generate_password
from .config import Config, VaultManager, CONFIG_FILE
from .vault import Vault
from .cli import vault as vault_module

WARNING_MESSAGE = \
    f"""
WARNING: YOU WON'T BE ABLE TO ACCESS YOUR VAULT WITHOUT THIS PASSWORD.
Notice: You'll need the salt value to access this vault in another system.
Don't forget to copy {CONFIG_FILE} file.
    """

config = Config()
vaultmanager = VaultManager(config)

class VaultNotFoundError(click.ClickException):
    """
    Raised when requested vault not found.
    """

def get_vault(name=None):
    if name is None and vaultmanager.default_vault is None:
        raise VaultNotFoundError("Vault is not found and default vault is empty.")

    if name is None:
        return Vault(vaultmanager.vaults[vaultmanager.default_vault])

    try:
        return Vault(vaultmanager.vaults[name])
    except KeyError:
        raise VaultNotFoundError("Vault is not found.")



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
@click.option("--vault", default=None, help="Pick a vault to put your password in (business, social_media, etc.)")
@click.argument("password_identifier")
def save(vault, password_identifier):
    """Save your passwords into your vaults"""
    vault_object = get_vault(vault)

    vault_password = click.prompt("Enter your vault password for your vault", hide_input=True)
    password = click.prompt("Enter your password", hide_input=True)
    password_repetition = click.prompt("Enter your password again", hide_input=True)

    if password == password_repetition:
        tmp = vault_object.passwords.copy()
        tmp[password_identifier] = password
        vault_object.passwords = tmp
        click.echo("Password has been saved!")
    else:
        click.echo("Please make sure you did write the same passwords")


@cli.group()
def vault():
    pass

vault.add_command(vault_module.add)
vault.add_command(vault_module.remove)
vault.add_command(vault_module.create)


def main():
    cli()

if __name__ == "__main__":
    
    main()
