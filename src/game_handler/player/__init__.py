"""The player class"""
from pygame.math import Vector2
from pygame.surface import Surface
from src.game_handler.inventory import Inventory
from src.game_handler.items import Log
from pygame.sprite import Sprite
from pygame.locals import K_w, K_s, K_a, K_d, K_z, K_q, K_d
from src.functions import get_keyboard_layout

class Player(Sprite):
    """The player"""
    _health: int
    _hunger: int
    inventory: Inventory
    movement: Vector2 = Vector2(0, 0)


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
        super().__init__()
        self.image = Surface((32, 32))
        self.image.fill("Red")
        self.rect = self.image.get_rect()
        self.inventory = Inventory()
        self.health = health
        self.hunger = hunger

    def events(self, event):
        # movements
        self.movement = Vector2(0, 0)
        if event[K_w if get_keyboard_layout() == "QWERTY" else K_z]:
            self.movement.y = -1
        if event[K_s if get_keyboard_layout() == "QWERTY" else K_s]:
            self.movement.y = 1
        if event[K_a if get_keyboard_layout() == "QWERTY" else K_q]:
            self.movement.x = -1
        if event[K_d if get_keyboard_layout() == "QWERTY" else K_d]:
            self.movement.x = 1

        self.movement = self.movement.normalize() if self.movement.length() > 0 else self.movement

    def update(self, delta):
        self.rect.move_ip(self.movement * delta * 250)

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
