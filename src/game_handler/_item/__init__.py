"""Base Item class"""


class Item:
    """A game item"""

    @property
    def name(self) -> str:
        """The name of the item"""
        return self.__class__.__name__.replace("_", " ")

    @property
    def description(self) -> str:
        """The description of the item"""
        return self.__doc__

    def __str__(self):
        return f"{self.name} ({self.description[:19] + '…' if len(self.description) > 20 else self.description})"

    def __repr__(self):
        return str(self)


class Recipe:
    """A recipe for crafting items"""
    ingredients: dict[type[Item], int]
    duration: int
    result: type[Item]

    def __init__(self, ingredients: dict[type[Item], int], duration: int, result: type[Item]):
        self.ingredients = ingredients
        self.duration = duration
        self.result = result


class Craftable(Item):
    """A craftable item"""
    recipy: Recipe
    duration: int
