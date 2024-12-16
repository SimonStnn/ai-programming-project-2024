"""The player class"""
from typing import TypedDict

import pygame.image
from pygame.math import Vector2
from pygame.surface import Surface
from pygame.sprite import Sprite
from pygame.key import ScancodeWrapper
from pygame.locals import K_w, K_s, K_a, K_d, K_z, K_q, K_d

from src.game_handler.inventory import Inventory
from src.game_handler.items import Log
from src.functions import get_keyboard_layout


class PlayerStats(TypedDict):
    health: int
    hunger: int
    score: int


class Player(Sprite):
    """The player"""
    stats: PlayerStats = {
        "health": 100,
        "hunger": 100,
        "score": 0,
    }
    inventory: Inventory
    movement: Vector2 = Vector2(0, 0)

    @property
    def health(self):
        """The player's health"""
        return self.stats["health"]

    @health.setter
    def health(self, value: int):
        self.stats["health"] = max(0, min(value, 100))

    @property
    def hunger(self):
        """The player's hunger"""
        return self.stats["hunger"]

    @hunger.setter
    def hunger(self, value: int):
        self.stats["hunger"] = max(0, min(value, 100))

    @property
    def pos(self):
        return self.rect.x, self.rect.y
    
    def take_damage(self, damage: int):
        """Take player damage"""
        self.health -= damage
        if self.health <= 0:
            # self.kill()  # Assuming you want to remove the player when health is 0
            ...


    def __init__(self, *, health: int = 100, hunger: int = 100):
        super().__init__()

        self.base_image = pygame.image.load("images/Characters/Human/WALKING/base_walk_strip8.png")
        self.animations = {
            0: self.base_image.subsurface((0, 0, 96, 64)),
            1: self.base_image.subsurface((96, 0, 96, 64)),
            2: self.base_image.subsurface((96*2, 0, 96, 64)),
            3: self.base_image.subsurface((96*3, 0, 96, 64)),
            4: self.base_image.subsurface((96*4, 0, 96, 64)),
            5: self.base_image.subsurface((96*5, 0, 96, 64)),
            6: self.base_image.subsurface((96*6, 0, 96, 64)),
            7: self.base_image.subsurface((96*7, 0, 96, 64)),
        }
        self.animation_speed = 20
        self.animation_index = 0
        self.is_flip = False
        self.image = self.animations[self.animation_index]
        self.rect = self.image.get_rect()
        self.inventory = Inventory()
        self.health = health
        self.hunger = hunger

    def update_animation(self, delta: int | float):
        self.animation_index += delta * self.animation_speed
        self.image = self.animations[int(self.animation_index) % 8]
        # make image bigger
        self.image = pygame.transform.scale(self.image, (96*2, 64*2))
        # flip the image if the player is moving left
        if self.movement.x < 0:
            self.is_flip = True
        if self.movement.x > 0:
            self.is_flip = False

        self.image = pygame.transform.flip(self.image, self.is_flip, False)
        self.rect = self.image.get_rect(center=self.rect.center)


    def increment_score(self, score: int):
        """Increment the player's score"""
        self.stats["score"] += score

    def get_score(self):
        """Get the player's score"""
        return self.stats["score"]

    def events(self, event: ScancodeWrapper):
        # movements
        self.movement = Vector2(0, 0)
        if event[K_w if get_keyboard_layout() == "QWERTY" else K_z]:
            self.movement.y = -1
        elif event[K_s if get_keyboard_layout() == "QWERTY" else K_s]:
            self.movement.y = 1
        if event[K_a if get_keyboard_layout() == "QWERTY" else K_q]:
            self.movement.x = -1
        elif event[K_d if get_keyboard_layout() == "QWERTY" else K_d]:
            self.movement.x = 1

        self.movement = self.movement.normalize() if self.movement.length() > 0 else self.movement
        self.rect.centerx += self.movement.x * 1.5
        self.rect.centery += self.movement.y * 1.5

    def update(self, delta: int | float):
        self.update_animation(delta)

    def update_scale(self, resolution): ...
    def heal(self, health: int):
        """Heal the player"""
        self.health += health

    def __str__(self):
        return f"Player Health: {self.health}, Hunger:{self.hunger}\n{self.inventory}"

    @pos.setter
    def pos(self, value):
        self.rect.centerx, self.rect.centery = value
        # Re-align the image's rect after moving
        self.rect = self.image.get_rect(center=self.rect.center)


if __name__ == "__main__":
    player = Player()

    log = Log()

    player.inventory.insert_item(log, 2, 1)
    player.inventory.append(Log())

    print(player)
