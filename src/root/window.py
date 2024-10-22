import pygame
from src.const import WINDOW_SIZE, SCALED, BLOCKSIZE
from src.game_handler.groups.visible_sprites import VisibleSprites
from src.level_handler import Level
from src.const import PREGENERATED_LEVEL
from src.game_handler.player import Player

class Window:
    running: bool
    screen: pygame.SurfaceType

    def __init__(self):
        self.running = False
        self.player = Player()
        self.visible_sprites = VisibleSprites(player=self.player)
        self.screen = pygame.display.set_mode(WINDOW_SIZE,pygame.HWACCEL | pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.SCALED)
        self.clock = pygame.Clock()
        # get keyboard type (QWERTY, AZERTY, QWERTZ)
        self.vsync = True
        self.delta = 0
        self.current_level = Level()
        self.current_level.update_map(PREGENERATED_LEVEL, BLOCKSIZE)



    def pre_draw_update(self):
        self.visible_sprites.update(self.delta)
        self.player.events(pygame.key.get_pressed())

    def draw(self):
        self.screen.fill("White")
        self.current_level.draw(self.screen)
        self.visible_sprites.draw(self.screen)
        pygame.display.flip()

    def post_draw_update(self):
        self.delta = self.clock.tick(pygame.display.get_desktop_refresh_rates()[0] if self.vsync else 60)

    def process_events(self):
        self.delta = self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    @staticmethod
    def update_caption(text=""):
        pygame.display.set_caption(text)

    def run(self):
        self.running = True
        while self.running:
            self.process_events()
            self.pre_draw_update()
            self.draw()
            self.post_draw_update()