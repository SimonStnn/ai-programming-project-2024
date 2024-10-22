import pygame
from src.const import WINDOW_SIZE, SCALED, BLOCKSIZE
from src.level_handler import Level
from src.const import PREGENERATED_LEVEL

class Window:
    running: bool
    screen: pygame.SurfaceType

    def __init__(self):
        self.running = False
        self.visible_sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.HWACCEL | pygame.DOUBLEBUF)
        self.clock = pygame.Clock()
        self.delta = 0
        self.current_level = Level()
        self.current_level.update_map(PREGENERATED_LEVEL, BLOCKSIZE)
        print(self.current_level)



    def pre_draw_update(self):
        ...

    def draw(self):
        self.screen.fill("White")
        self.current_level.draw(self.screen)
        self.visible_sprites.draw(self.screen)
        pygame.display.flip()

    def post_draw_update(self):
        self.delta = self.clock.tick(60)

    def process_events(self):
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