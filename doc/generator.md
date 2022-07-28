This document is a template for the development.

## Generate

**Command**: ``passgen generate``

**Options**:
```
--upper   Enable/Disable uppercase chars (ABC) | DEFAULT=True
--lower   Enable/Disable lowercase chars (abc) | DEFAULT=True
--numeric Enable/Disable numeric chars (123) | Default=True
--punct   Enable/Disable punctuation chars (@!?) | Default=True
--save    Save generated password to the vault.
```

### Example

```
passgen generate --save 
[jsh2hdi*&] Ok? [Enter/Tab]
Enter your main password for my_vault: *******
Enter a name for your new generated password: gh_pass
Password saved!
```

