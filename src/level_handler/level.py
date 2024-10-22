from src.const import BLOCKSIZE, SCALED
import pygame.surface
from src.level_handler.tile import Tile
from src.level_handler.level_enum import TileType

class Level:
    map: list[Tile|None] = list()

    def update_map(self, m: list[list[int]], blocksize: list[int]):
        self.map.clear()
        for y ,  row in enumerate(m):
            for x,  col in enumerate(row):
                self.__add_tile(col, (x * blocksize[0], y * blocksize[1]))

    @staticmethod
    def __get_type(tile: int):
        match tile:
            case 0 | _:
                return TileType.GRASS

    def __add_tile(self, tile: int, pos: tuple[int, int]):
        self.map.append(Tile(self.__get_img(tile), self.__get_type(tile),  pos))

    @staticmethod
    def __get_img(tile):
        return pygame.surface.Surface(BLOCKSIZE)

    def draw(self, screen):
        for x,tile in enumerate(self.map):
            tile.image.fill((x* 10 % 255, 0, 0))
            screen.blit(tile.image, tile.rect)

    def __str__(self):
        return str(self.map)

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    l = Level()
    l.update_map([[0, 0, 0], [0, 0, 0], [0, 0, 0]], BLOCKSIZE)
    print(l.map)