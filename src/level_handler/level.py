import pygame.surface

from src.level_handler.tile import Tile
from src.level_handler.level_enum import TileType

class Level:
    map: list[None|int] = list()

    def read_map(self, m: list[int]):
        for tile in m:
            self.map.append(Tile(self.__get_img(), self.__get_type(tile), self.__get_pos()))

    @staticmethod
    def __get_type(self, t: Tile):
        match t:
            case 0 | _:
                return TileType.GRASS


    @staticmethod
    def __get_img(self):
        return pygame.surface.Surface((80,20))

    @staticmethod
    def __get_pos(self):
        return (10,10)


    def __str__(self):
        return str(self.map)

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    l = Level()
    l.read_map([0, 1])
    print(l)