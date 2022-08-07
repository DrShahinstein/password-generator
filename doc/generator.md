## Generate

<p>Generate a strong password.</p>

**Command**: `passgen generate [OPTIONS]`

**Options**:

| Option                     | Description                              |                 |
| -------------------------- | ---------------------------------------- | --------------- |
| `--save`                   | Save your password into your vault       | `DEFAULT=False` |
| `--length INTEGER`         | Determine the length of the password     | `DEFAULT=8`     |
| `--upper / --no-upper`     | Enable/Disable uppercase chars `(ABC)`   | `DEFAULT=True`  |
| `--lower / --no-lower`     | Enable/Disable lowercase chars `(abc)`   | `DEFAULT=True`  |
| `--numeric / --no-numeric` | Enable/Disable numeric chars `(123)`     | `DEFAULT=True`  |
| `--punct / --no-punct`     | Enable/Disable punctuation chars `(@!?)` | `DEFAULT=True`  |
| `--help`                   | Shows the help menu                      | `DEFAULT=False` |

### Example

```
passgen generate --save
[jsh2hdi*&] Ok? [y/N]:
Enter your password to my_vault: *******
Enter a name for your new generated password: gh_pass
Password saved!
```
