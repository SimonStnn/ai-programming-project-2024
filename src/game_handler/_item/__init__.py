class Item:
    description: str

    @property
    def name(self):
        return self.__class__.__name__.replace("_", " ")

    def __str__(self):
        return f"{self.name} ({self.description})"

    def __repr__(self):
        return str(self)
