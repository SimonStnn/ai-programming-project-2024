# src/root/main_game.py
import pygame
from pygame.key import get_pressed
from src.game_handler.entity import Player
from src.map import TILE_TRANSLATIONS
from src.map.map import generate_empty_map, seed_map, get_map_chunk, Tile
from src.game_handler.Camera import CameraGroup
import threading
from src.game_handler.entity.enemy import EnemyHandler

class MainGame:
    player: Player
    visible_sprites: CameraGroup
    delta: float

    def __init__(self, master):
        self.master = master
        self.player = Player()
        self.my_map = generate_empty_map([1000, 1000])
        self.current_chunk = None
        self.start_pos = [self.my_map.shape[0] // 2, self.my_map.shape[1] // 2]
        self.visible_sprites = CameraGroup(
            player=self.player,
            screen_width=pygame.display.get_window_size()[0],
            screen_height=pygame.display.get_window_size()[1],
            map_width=self.my_map.shape[0] * 32,
            map_height=self.my_map.shape[1] * 32
        )
        self.visible_sprites.add(self.player)
        self.delta = 0
        self.enemy_handler = EnemyHandler(self.player)

    def chunk_update(self):
        self.my_map = seed_map(
            self.my_map,
            (self.start_pos[0] + self.player.pos[0], self.start_pos[1] + self.player.pos[1]),
            (int(pygame.display.get_window_size()[0] // 32 * 2), int(pygame.display.get_window_size()[1] // 32 * 2))
        )
        self.current_chunk = get_map_chunk(
            self.my_map,
            (self.start_pos[0] + self.player.pos[0], self.start_pos[1] + self.player.pos[1]),
            (int(pygame.display.get_window_size()[0] // 32 * 2), int(pygame.display.get_window_size()[1] // 32 * 2))
        )

    def pre_draw_update(self):
        self.delta = self.master.clock.tick(self.master.fps) / 1000.0
        self.visible_sprites.update(self.delta)
        self.player.events(get_pressed())
        if self.current_chunk is None:
            self.chunk_update()

        # dont thread if its active
        if not threading.active_count() > 1: threading.Thread(target=self.chunk_update, name="map").start()
        self.enemy_handler.update(self.delta)

    def update_scale(self, resolution):
        self.visible_sprites.update_scale(resolution)

    def draw(self):
        self.master.screen.fill("White")
        self.visible_sprites.sprites().clear()
        spl = []
        for x in range(self.current_chunk.shape[0]):
            for y in range(self.current_chunk.shape[1]):
                if x < self.current_chunk.shape[0] and y < self.current_chunk.shape[1]:
                    tile: Tile = TILE_TRANSLATIONS[self.current_chunk[x, y]]
                    self.master.screen.blit(tile["sprite"], (x * 32 - self.visible_sprites.offset.x, y * 32 - self.visible_sprites.offset.y))

        self.visible_sprites.draw(self.master.screen)
        self.enemy_handler.draw(self.master.screen, self.visible_sprites.offset)


    def post_draw_update(self): ...

    def process_events(self, event):
        pass