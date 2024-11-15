import pygame, numpy as np
from pygame.key import get_pressed
from src.game_handler.entity import Player
from src.game_handler.groups.visible_sprites import VisibleSprites
from src.map import TILE_TRANSLATIONS
from src.map.map import generate_empty_map, seed_map, get_map_chunk, Tile



class MainGame:
    player: Player
    visible_sprites: VisibleSprites
    delta: float

    def __init__(self, master):
        self.master = master
        self.player = Player()
        self.my_map = generate_empty_map([1000, 1000])
        self.start_pos = [self.my_map.shape[0] // 2, self.my_map.shape[1] // 2]
        self.visible_sprites = VisibleSprites(player=self.player)
        self.delta = 0

    def pre_draw_update(self):
        self.visible_sprites.update(self.delta)
        self.player.events(get_pressed())

    def update_scale(self, resolution):
        self.visible_sprites.update_scale(resolution)

    def draw(self):
        self.master.screen.fill("White")
        chunk = get_map_chunk(
            self.my_map,
            (self.start_pos[0] + self.player.pos[0], self.start_pos[1] + self.player.pos[1]),
            (int(pygame.display.get_window_size()[0] // 32 * 1.25), int(pygame.display.get_window_size()[1] // 32 *1.25))
        )
        # in this case the chunk is [25, 18]
        for x in range(chunk.shape[0]):
            for y in range(chunk.shape[1]):
                tile: Tile = TILE_TRANSLATIONS[chunk[x, y]]
                self.master.screen.blit(tile["sprite"], (x * 32, y * 32))

        self.visible_sprites.draw(self.master.screen)

    def post_draw_update(self):
        self.delta = self.master.clock.tick(self.master.fps) / 1000
        self.my_map = seed_map(
            self.my_map,
            (self.start_pos[0] + self.player.pos[0], self.start_pos[1] + self.player.pos[1]),
            (int(pygame.display.get_window_size()[0] // 32 * 1.25), int( pygame.display.get_window_size()[1] // 32*1.25))

        )
        # np.savetxt('./src/map/map.txt', self.my_map, fmt='%d')

    def process_events(self, event):
        pass
