from src.game_handler.inventory import Inventory


class Player:
    health: int
    hunger: int
    inventory: Inventory 

    def __init__(self, *, health: int = 100, hunger: int = 100):
        self.inventory = Inventory()
        self.health = health
        self.hunger = hunger
