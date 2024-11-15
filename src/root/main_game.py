import pygame, numpy as np
from pygame.key import get_pressed
from src.game_handler.player import Player
from src.game_handler.groups.visible_sprites import VisibleSprites
from src.map.map import generate_empty_map, seed_map, get_map_chunk

class MainGame:
    player: Player
    visible_sprites: VisibleSprites
    delta: float

    def __init__(self, master):
        self.master = master
        self.player = Player()
        self.my_map = generate_empty_map([1000, 1000])
        start_pos = [self.my_map.shape[0]//2, self.my_map.shape[1]//2]
        self.visible_sprites = VisibleSprites(player=self.player)
        self.delta = 0


    def pre_draw_update(self):
        self.visible_sprites.update(self.delta)
        self.player.events(get_pressed())

    def update_scale(self, resolution):
        self.visible_sprites.update_scale(resolution)

    def draw(self):
        self.master.screen.fill("White")
        start_pos = [int(self.player.rect.x), int(self.player.rect.y)]
        chunk_range = [pygame.display.get_surface().get_width()//32, pygame.display.get_surface().get_height()//32]
        chunk = get_map_chunk(self.my_map, start_pos, chunk_range)
        for x in range(chunk.shape[0]):
            for y in range(chunk.shape[1]):
                if chunk[x, y] == 1:
                    pygame.draw.rect(self.master.screen, "Green", (x*32, y*32, 32, 32))
                elif chunk[x, y] == 2:
                    pygame.draw.rect(self.master.screen, "Yellow", (x*32, y*32, 32, 32))
                elif chunk[x, y] == 3:
                    pygame.draw.rect(self.master.screen, "Blue", (x*32, y*32, 32, 32))
        self.visible_sprites.draw(self.master.screen)
        # draw map


    def post_draw_update(self):
        self.delta = self.master.clock.tick(self.master.fps) / 1000
        self.my_map = seed_map(self.my_map, (self.player.rect.x, self.player.rect.y), (32, 32))
        # np.savetxt('./src/map/map.txt', self.my_map, fmt='%d')

    def process_events(self, event):
        pass
