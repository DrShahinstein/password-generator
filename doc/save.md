# Save

<p>Save your passwords into your vaults.</p>

**Command**: `passgen save [OPTIONS] [ARGUMENTS]`

**Options**

| Option          | Description           |               |
| --------------- | --------------------- | ------------- |
| `--vault vault` | Choose a unique vault | DEFAULT=False |
| `--help`        | Shows the help menu   | DEFAULT=False |

**Arguments**

| Argument              | Description                  |
| --------------------- | ---------------------------- |
| `PASSWORD_IDENTIFIER` | A name for the new password. |

**Example**

```
$ passgen save google_password
Enter your vault password for your vault my_vault: *********
Enter your password: ******
Enter your password again: ******
Password has been saved!
```
