This document is a template for the development.

## Generate

**Command**: passgen generate

**Options**:

--no-upper _No uppercase_
--no-lower _No lowercase_
--no-numeric _No numeric characters_
--no-punct _No punctuation_
--save _Save generated password to the vault._

### Example

```
passgen generate --save --no-upper
[jsh2hdi*&] Ok? [Enter/Tab]
Enter your main password for my_vault: *******
Enter a name for your new generated password: gh_pass
Password saved!
```

