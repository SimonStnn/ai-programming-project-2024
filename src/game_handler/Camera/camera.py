import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self, player, screen_width, screen_height):
        super().__init__()
        self.player = player
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = pygame.math.Vector2()

    def update(self, *args):
        super().update(*args)
        self.offset.x = self.player.rect.centerx + self.screen_width // 2
        self.offset.y = self.player.rect.centery + self.screen_height // 2

    def draw(self, surface):
        for sprite in self.sprites():
            if self.player is not sprite:
                offset_pos = sprite.rect.topleft - self.offset
                surface.blit(sprite.image, offset_pos)
        surface.blit(self.player.image, (self.screen_width // 2, self.screen_height // 2))