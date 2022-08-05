# Vault Remove

<p>Remove given vault from known vaults.</p>

**Command**: `passgen vault remove [OPTIONS] [ARGUMENTS]`

**Options**

| Option   | Description         |                 |
| -------- | ------------------- | --------------- |
| `--help` | Shows the help menu | `DEFAULT=False` |

**Arguments**

| Argument     | Description                                      |
| ------------ | ------------------------------------------------ |
| `VAULT_NAME` | The vault name which is going to be removed soon |

## Example

```
passgen vault remove vaultname
Are you sure you want to remove vaultname from the existing vaults?
You won't be able to use it unless you add it again. [y/N]

Vault removed from the existing vaults.
Done.
```
