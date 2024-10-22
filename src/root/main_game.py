from pygame.key import get_pressed
from src.game_handler.player import Player
from src.game_handler.groups.visible_sprites import VisibleSprites
from src.level_handler import Level
from src.const import generate_level, block_size

class MainGame:
    current_level: Level
    player: Player
    visible_sprites: VisibleSprites
    delta: float

    def __init__(self, master):
        self.master = master
        self.player = Player()
        self.visible_sprites = VisibleSprites(player=self.player)
        self.reset_map()
        self.delta = 0

    def reset_map(self):
        self.current_level = Level()
        self.current_level.update_map(generate_level(), block_size(self.master.screen.get_size()))

    def pre_draw_update(self):
        self.visible_sprites.update(self.delta)
        self.player.events(get_pressed())

    def draw(self):
        self.master.screen.fill("White")
        self.current_level.draw(self.master.screen)
        self.visible_sprites.draw(self.master.screen)

    def post_draw_update(self):
        pass

    def process_events(self, event):
        pass
