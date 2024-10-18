"""The player class"""
from src.game_handler.inventory import Inventory
from src.game_handler.items import Log


class Player:
    """The player"""
    _health: int
    _hunger: int
    inventory: Inventory

    @property
    def health(self):
        """The player's health"""
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = max(0, min(value, 100))

    @property
    def hunger(self):
        """The player's hunger"""
        return self._hunger

    @hunger.setter
    def hunger(self, value: int):
        self._hunger = max(0, min(value, 100))

    def __init__(self, *, health: int = 100, hunger: int = 100):
        self.inventory = Inventory()
        self.health = health
        self.hunger = hunger

    def take_damage(self, damage: int):
        """Take player damage"""
        self.health -= damage

    def heal(self, health: int):
        """Heal the player"""
        self.health += health

    def __str__(self):
        return f"Player Health: {self.health}, Hunger:{self.hunger}\n{self.inventory}"


if __name__ == "__main__":
    player = Player()

    log = Log()

    player.inventory.insert_item(log, 2, 1)
    player.inventory.append(Log())

    print(player)
