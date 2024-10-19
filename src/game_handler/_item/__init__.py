"""Base Item class"""
from typing import TYPE_CHECKING
from abc import ABC
from attrs import define

if TYPE_CHECKING:
    from src.game_handler.player import Player


@define
class Item(ABC):
    """A game item"""

    @classmethod
    def name(cls) -> str:
        """The name of the item"""
        return cls.__name__.replace("_", " ")

    @classmethod
    def description(cls) -> str:
        """The description of the item"""
        return cls.__doc__


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


class Interactable(Item):
    """An interactable item"""

    def interact(self, player: "Player"):
        pass


class Consumable(Interactable):
    """A consumable item"""

    heals: int
    hunger: int

    def consume(self, player: "Player"):
        player.heal(self.heals)
        player.hunger += self.hunger
