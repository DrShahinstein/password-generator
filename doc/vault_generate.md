# Create a Vault

<p>Creates a new vault</p>

**Command**: `passgen vault create [OPTIONS] [ARGUMENTS]`

**Options**

| Option   | Description         |                 |
| -------- | ------------------- | --------------- |
| `--help` | Shows the help menu | `DEFAULT=False` |

## Arguments

| Argument     | Description                            |
| ------------ | -------------------------------------- |
| `VAULT_NAME` | A name for the vault                   |
| `VAULT_PATH` | The path of the vault `(not required)` |

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
