from enum import Enum
from random import randint


class Animals(Enum):
    BIRD = "bird"
    CHICKEN = "chicken"
    COW = "cow"
    DUCK = "duck"
    PIG = "pig"
    SHEEP = "sheep"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __add__(self, other):
        return self.value + other


RESOLUTIONS = [
    (1280, 720),
    (1920, 1080)
]
WORLD_SIZE = (20, 20)

def generate_level():
    return [[randint(0, 5) for _ in range(WORLD_SIZE[0])] for _ in range(WORLD_SIZE[1])]

def block_size(resolution):
    return resolution[0] // WORLD_SIZE[0], resolution[1] // WORLD_SIZE[1]
