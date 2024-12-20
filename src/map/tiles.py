import pygame
from typing import TypedDict
from src.functions import img_path


class Tile(TypedDict):
    name: str
    level: int
    sprite: pygame.Surface


def get_tile(name: str, ext: str = ".jpg", level: int = 1) -> Tile:
    return {
        "name": name,
        "level": level,
        "sprite": pygame.transform.smoothscale(pygame.image.load(img_path(f"Tileset/{name}{ext}") or "Tileset/missing.png"), (32,32))  # type: ignore
    }


TILE_TRANSLATIONS: dict[int, Tile] = {
    0: get_tile(name="dirt"),
    1: get_tile(name="grass"),
    2: get_tile(name="sand"),
    3: get_tile(name="water", level=0)
}
