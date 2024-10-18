import pygame
from src.const import WINDOW_SIZE


class Window:
    running: bool
    screen: pygame.SurfaceType

    def __init__(self):
        self.running = False
        self.screen = pygame.display.set_mode(WINDOW_SIZE)


    def run(self):
        self.running = True
        s = pygame.Surface((20,20))
        s.fill("cyan")
        r = s.get_rect()
        r.center = (20 ,20)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")
            self.screen.blit(s, r)
            r.centery
            pygame.display.flip()