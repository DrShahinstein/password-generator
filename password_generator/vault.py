"""
Json example

{
    "name": "pass",
    "name2": "pass2",
    ...
}
"""
import json
import os
from pathlib import Path

DEFAULT_VAULT_FOLDER = Path(os.environ['HOME']) / "PasswordVaults"


class Vault:
    def __init__(self, filename):
        self.filename = filename

    @property
    def passwords(self):
        return self._load_content()

    @passwords.setter
    def passwords(self, new):
        self._update_content(new)

    def _load_content(self):
        with open(self.filename) as f:
            content = json.load(f)

        return content
    
    def _update_content(self, new_content):
        with open(self.filename, 'w') as f:
            json.dump(new_content, f)


    @staticmethod 
    def create_vault(name, filename=None):
        if filename is None:
            if not os.path.exists(DEFAULT_VAULT_FOLDER):
                os.mkdir(DEFAULT_VAULT_FOLDER)

            path = str(DEFAULT_VAULT_FOLDER / name)

            while os.path.exists(path):
                path += "1"


        else:
            path = filename

        with open(path, "w") as f:
            json.dump({}, f)

        return path

    def add_password(self, identifier, password):
        if identifier.strip() == "" or password.strip() == "":
            raise ValueError("Password or identifier cannot be empty.")
        self.passwords[identifier] = password
        _update_content()
        

