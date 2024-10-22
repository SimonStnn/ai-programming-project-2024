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


WINDOW_SIZE = (800, 600)


BLOCKSIZE = (32, 32)

# blocksize scaled to the window size
SCALED = (WINDOW_SIZE[0] // BLOCKSIZE[0], WINDOW_SIZE[1] // BLOCKSIZE[1])
# to fully fill the screen you need a list[list[int]] with the same dimensions as SCALED
PREGENERATED_LEVEL = [[ randint(0,5) for _ in range(SCALED[0] + 1)] for _ in range(SCALED[1] + 1)]