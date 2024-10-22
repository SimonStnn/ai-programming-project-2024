from pygame.display import get_surface
from pygame.key import get_pressed
from src.game_handler.player import Player
from src.game_handler.groups.visible_sprites import VisibleSprites
from src.level_handler import Level
from src.const import PREGENERATED_LEVEL, BLOCKSIZE

class MainGame:
    def __init__(self):
        self.screen = get_surface()
        self.player = Player()
        self.visible_sprites = VisibleSprites(player=self.player)
        self.current_level = Level()
        self.current_level.update_map(PREGENERATED_LEVEL, BLOCKSIZE)
        self.delta = 0

    def pre_draw_update(self):
        self.visible_sprites.update(self.delta)
        self.player.events(get_pressed())

    def draw(self):
        self.screen.fill("White")
        self.current_level.draw(self.screen)
        self.visible_sprites.draw(self.screen)
