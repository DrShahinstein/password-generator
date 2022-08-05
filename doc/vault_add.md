# Add Vault

<p>Adds your existing vault into the config</p>

**Command**: `passgen vault add [OPTIONS] [ARGUMENTS]`

**Options**

| Option   | Description         |                 |
| -------- | ------------------- | --------------- |
| `--help` | Shows the help menu | `DEFAULT=False` |

**Arguments**

| Argument | Description                                             |
| -------- | ------------------------------------------------------- |
| `PATH`   | The path representing the file which includes the vault |

## Example

```
$ passgen vault add /path/to/file
Enter a name for this vault: business_vault
Set business_vault as a default vault? [y/N]: N
Done!
```
