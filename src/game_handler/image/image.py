from collections.abc import Sequence
from pygame.surface import SurfaceType
from pygame.image import load
from pygame.transform import smoothscale

class Image:
    __image: SurfaceType
    def __init__(self, url: str, size: Sequence[float]):
        self.__image = smoothscale(load(url), size)

    def __repr__(self):
        return self.__image

    def __str__(self):
        return str(self.__image)
