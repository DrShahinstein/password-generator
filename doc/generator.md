This document is a template for the development.

## Generate

**Command**: ``passgen generate``

**Options**:
```
--no-upper   No uppercase
--no-lower   No lowercase
--no-numeric No numeric characters
--no-punct   No punctuation
--save       Save generated password to the vault.
```

### Example

```
passgen generate --save --no-upper
[jsh2hdi*&] Ok? [Enter/Tab]
Enter your main password for my_vault: *******
Enter a name for your new generated password: gh_pass
Password saved!
```

