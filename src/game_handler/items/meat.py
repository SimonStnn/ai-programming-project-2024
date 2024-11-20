from src.game_handler.items import Item, Consumable, Interactable


class Meat(Consumable, Interactable, Item):
    """Some tasty meat"""

    heals: int = 10
    hunger: int = 20
