class Option:
    def __init__(self, name, type, description, required=False, choices=None):
        self.name = name
        self.type = type
        self.description = description
        self.required = required
        self.choices = choices or []

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "required": self.required,
            "choices": self.choices
        }
