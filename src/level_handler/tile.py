from pygame.surface import Surface
from pygame.sprite import Sprite


class Tile(Sprite):
    def __init__(self, img, tp, pos):
        super().__init__()
        self.image = img
        self.type = tp
        self.rect = self.image.get_rect(topleft=pos)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Tile:{self.type=}, @{self.rect.center=}"


if __name__ == "__main__":
    t = Tile(Surface((10, 10)), "grass", (10, 10))
    print(t)
