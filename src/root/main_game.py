from pygame.key import get_pressed
from src.game_handler.player import Player
from src.game_handler.groups.visible_sprites import VisibleSprites

class MainGame:
    player: Player
    visible_sprites: VisibleSprites
    delta: float

    def __init__(self, master):
        self.master = master
        self.player = Player()
        self.visible_sprites = VisibleSprites(player=self.player)
        self.delta = 0


    def pre_draw_update(self):
        self.visible_sprites.update(self.delta)
        self.player.events(get_pressed())

    def update_scale(self, resolution):
        self.visible_sprites.update_scale(resolution)

    def draw(self):
        self.master.screen.fill("White")
        self.visible_sprites.draw(self.master.screen)

    def post_draw_update(self):
        pass

    def process_events(self, event):
        pass
