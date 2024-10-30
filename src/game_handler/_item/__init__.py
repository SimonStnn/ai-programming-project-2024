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
    @property
    def name(cls) -> str:
        """The name of the item"""
        return cls.__name__.replace("_", " ")

    @classmethod
    @property
    def description(cls) -> str:
        """The description of the item"""
        return cls.__doc__

    def __eq__(self, other):
        if other == type(self):
            return True
        return super().__eq__(other)


@define
class Recipe:
    """A recipe for crafting items"""
    ingredients: dict[type[Item], int]
    duration: int
    result: dict[type[Item], int]


class Craftable(Item):
    """A craftable item"""
    duration: int = field(
        converter=int,
        validator=[validators.instance_of(int), validators.ge(0)],
        default=0
    )

    @property
    @abstractmethod
    def recipe(self) -> Recipe:
        ...

    @property
    def result(self) -> dict[type[Item], int]:
        return self.recipe.result

    def craft(self, player: "Player"):
        if all(player.inventory.contains(ingredient, quantity) for ingredient, quantity in
               self.recipe.ingredients.items()):
            for ingredient, quantity in self.recipe.ingredients.items():
                player.inventory.remove_item(ingredient, quantity)
            player.inventory.append(self.recipe.result)

        player.inventory.contains(self.recipe.ingredients)
        player.inventory.append(self.recipe.result)


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
