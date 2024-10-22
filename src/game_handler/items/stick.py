from src.game_handler.items import Item, Craftable, Recipe, Log


class Stick(Craftable, Item):
    """A stick"""

    duration = 0

    @property
    def recipe(self) -> Recipe:
        return Recipe(
            ingredients={Log: 1},
            duration=self.duration,
            result={Stick: 1},
        )
