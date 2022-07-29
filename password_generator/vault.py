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

        
