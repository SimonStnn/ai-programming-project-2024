from src.game_handler.items import Item, Craftable, Recipe, Log


class Stick(Craftable, Item):
    """A stick"""

recipe = Recipe({Log: 1}, 1, Stick)
