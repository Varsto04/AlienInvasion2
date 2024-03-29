import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship3.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.radius = 40
        #pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.rect.x -= 1
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
