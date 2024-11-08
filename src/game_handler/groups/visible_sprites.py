from pygame.sprite import Group

class VisibleSprites(Group):
    def __init__(self, *a, player):
        super().__init__([*a, player])
        self.player = player

    def update(self, delta):
        for sprite in self.sprites():
            if sprite != self.player: sprite.update()
            else: sprite.update(delta)


            sprite.rect.clamp_ip(sprite.rect)

    def update_scale(self, resolution):
        for sprite in self.sprites():
            sprite.update_scale(resolution)