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
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1920, 1080)
]

BLOCKSIZE = (32, 32)

# blocksize scaled to the window size
def scale_to_window( resolution):
    return resolution[0] // BLOCKSIZE[0], resolution[1] // BLOCKSIZE[1]
# to fully fill the screen you need a list[list[int]] with the same dimensions as SCALED
def pregenerate_level(scaled):
    return [[randint(0, 4) for _ in range(scaled[0])] for _ in range(scaled[1])]
