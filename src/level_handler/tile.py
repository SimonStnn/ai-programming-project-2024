from pygame.surface import Surface
from pygame.sprite import Sprite


class Tile(Sprite):
    def __init__(self, img, tp, pos):
        super().__init__()
        self.image = img
        self.type = tp
        self.rect = self.image.get_rect(topleft=pos)

    def update_size(self, blocksize):
        self.rect.size = blocksize
        self.image = Surface(blocksize)
        self.image.fill(self.__get_color(self.type))

    @staticmethod
    def __get_color(tile):
        match tile:
            case 0:
                return (0, 255, 0)
            case 1:
                return (0, 0, 255)
            case 2:
                return (255, 0, 0)
            case 3:
                return (255, 255, 0)
            case 4:
                return (255, 0, 255)
            case 5:
                return (0, 255, 255)
            case 6:
                return (255, 255, 255)
            case 7:
                return (0, 0, 0)
            case _:
                return (0, 0, 0)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Tile:{self.type=}, @{self.rect.topleft=}"




if __name__ == "__main__":
    t = Tile(Surface((10, 10)), "grass", (10, 10))
    print(t)
