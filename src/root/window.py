import pygame
from src.const import WINDOW_SIZE


class Window:
    running: bool
    screen: pygame.SurfaceType

    def __init__(self):
        self.running = False
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.HWACCEL | pygame.DOUBLEBUF)
        self.clock = pygame.Clock()
        self.delta = 0



    def pre_draw_update(self):
        ...

    def draw(self):
        ...

    def post_draw_update(self):
        ...

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