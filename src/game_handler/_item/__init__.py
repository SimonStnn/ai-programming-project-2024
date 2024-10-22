"""Base Item class"""
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from attrs import define, field, validators

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


@define
class Recipe:
    """A recipe for crafting items"""
    ingredients: dict[type[Item], int]
    duration: int
    result: dict[type[Item], int]


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
