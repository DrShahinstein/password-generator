import click
from ..config import VaultManager, Config
from ..vault import Vault

config = Config()
vaultmanager = VaultManager(config)


@click.command()
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


@click.command()
@click.argument("vault_name")
@click.argument("path", required=False, type=click.Path(exists=True))
def create(vault_name, path):
    """Creates a new vault"""
    from ..__init__ import WARNING_MESSAGE, validated_password_prompt

    click.echo("Creating a new vault...")
    while True:
        vault_password = validated_password_prompt(
            prompt_text="Enter the password for your new vault",
        )
        
        click.echo(WARNING_MESSAGE)
        new_path = Vault.create_vault(vault_name, path)
        is_default = click.confirm(f"Set {vault_name} as your default vault?")
        
        if is_default:
            vaultmanager.default_vault = vault_name
            
        config.config['vaults'][vault_name] = new_path
        config.save()
        click.echo("Done!")
        break


@click.command()
@click.argument("vault_name")
def remove(vault_name):
    """Removes a vault"""

    is_proceed = click.confirm(
        f"Are you sure you want to remove {vault_name} from the existing vaults?\n"
        "You won't be able to use it unless you add it again.")
    if is_proceed:
        tmp = vaultmanager.vaults
        try:
            if vaultmanager.vaults[vault_name] == vaultmanager.default_vault:
                vaultmanager.default_vault = None
            del tmp[vault_name]
            
        except KeyError:
            click.echo("Error: Vault doesn't exist.\nTerminating.")
            return

        vaultmanager.vaults = tmp
        click.echo("Vault removed from the existing vaults.")
        click.echo("Done.")
    else:
        click.echo("Terminated.")


@click.command()
def list():
    """Lists the whole existing vaults"""
    
    for name, path in vaultmanager.vaults.items():
        click.echo(f"??? {name}     {path}")
