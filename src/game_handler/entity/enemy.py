from pygame.sprite import Sprite, Group
from pygame.surface import Surface

class Enemy(Sprite):
    def __init__(self, target, speed=1):
        super().__init__()
        self.image = Surface((32, 32))
        self.image.fill("blue")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.target = target
        self.speed = speed

    def update(self, delta):
        if self.target.rect.x > self.rect.x:
            self.rect.x += self.speed * delta
        elif self.target.rect.x < self.rect.x:
            self.rect.x -= self.speed * delta
        if self.target.rect.y > self.rect.y:
            self.rect.y += self.speed * delta
        elif self.target.rect.y < self.rect.y:
            self.rect.y -= self.speed * delta
        # check collision
        if self.rect.colliderect(self.target.rect):
            self.target.take_damage(10)  # Assuming the player has a take_damage method
            self.kill()

class EnemyHandler(Group):
    def __init__(self, target):
        super().__init__()
        self.target = target

    def add_enemy(self):
        enemy = Enemy(self.target)
        self.add(enemy)

    def update(self, delta):
        # add enemies
        if len(self.sprites()) < 10:
            self.add_enemy()
        for enemy in self:
            enemy.update(delta)

    def draw(self, screen, offset):
        for enemy in self:
            print(enemy.rect.x - offset.x, enemy.rect.y - offset.y)
            screen.blit(enemy.image, (enemy.rect.x - offset.x, enemy.rect.y - offset.y))