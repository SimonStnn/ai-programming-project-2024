import pygame
import src.game_handler.Player

screen = pygame.display.set_mode((800,600), pygame.HWACCEL | pygame.DOUBLEBUF)
running = True
surf = pygame.Surface((80,60))
surf.fill("blue")
r = surf.get_rect()
r.center = (400,300)
clock = pygame.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    screen.blit(surf, r)
    pygame.display.flip()
