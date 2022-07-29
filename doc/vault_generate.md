# Generate Vault

## Arguments

```
VAULT_NAME      Name for the vault.
VAULT_PATH      Path of the vault (not required)
```

## Example

```
$ pass vault generate business_vault
Generating a new vault...
Enter a strong password for your vault: ************
Enter a strong password for your vault again: *********

WARNING: YOU WON'T BE ABLE TO ACCESS YOUR VAULT WITHOUT THIS PASSWORD.
Notice: You'll need the salt value to access this vault in another system.
Don't forget to copy /home/user/.config/password-manager/config.json file.

Vault Path: /home/user/Vaults/business_vault

Set business vault as your default vault? [y\N]: y
Done!
```
