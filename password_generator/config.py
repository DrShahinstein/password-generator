
import json
import os
from pathlib import Path
import io

logging_io = io.StringIO()

def generate_salt():
    return os.urandom(16)

EMPTY_CONFIG = {
    "salt": generate_salt().decode('LATIN-1'),
    "vaults": {},
    "default-vault": None,
}

CONFIG_FOLDER = Path(os.environ['HOME']) / Path(".config") / 'password-generator'
CONFIG_FILE = CONFIG_FOLDER / 'config.json'

if not os.path.exists(CONFIG_FOLDER):
    os.mkdir(CONFIG_FOLDER)

class ConfigError(Exception):
    pass

# I dont have much time to rewrite a better config manager, so:
# https://github.com/ramazanemreosmanoglu/living-logs/blob/main/src/config.py
# ~ ramazanemreosmanoglu

class Config:
    def __init__(self, file=CONFIG_FILE):
        self.file = file
        self.config = {}

        if not os.path.exists(self.file):
            self._generate_config()
            self.config = EMPTY_CONFIG
        else:
            # Load config
            self._load_config()

    def _generate_config(self):
        """Generate a new config with default values."""

        with open(self.file, 'x') as file:
            json.dump(EMPTY_CONFIG, file)

    def _load_config(self):
        with open(self.file, 'r') as file:
            try:
                self.config = json.load(file)
            except json.JSONDecodeError:
                raise ConfigError("Couldn't load config.")

    def save(self):
        """Saves self.config to the config file."""

        with open(self.file, 'w') as file:
            json.dump(self.config, file)



class VaultManager:
    def __init__(self, config):
        self.config = config

    @property
    def vaults(self):
        return self.config.config['vaults']

    @vaults.setter
    def vaults(self, new):
        self.config.config['vaults'] = new
        self.config.save()

    @property
    def default_vault(self):
        return self.config.config['default_vault']

    @default_vault.setter
    def default_vault(self, new):
        self.config.config['default_vault'] = new
        self.config.save()


