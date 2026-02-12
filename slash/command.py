class SlashCommand:
    def __init__(self, callback, name, description, options=None, whitelist=None, blacklist=None, ephemeral=False):
        self.callback = callback
        self.name = name
        self.description = description
        self.options = options or []
        self.whitelistRoles = whitelist or []
        self.blacklistRoles = blacklist or []
        self.ephemeral = ephemeral

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "options": [opt.to_dict() for opt in self.options],
            "whitelistRoles": self.whitelistRoles,
            "blacklistRoles": self.blacklistRoles,
            "ephemeral": self.ephemeral
        }
