import pygame
import sys
import Game, Level, Constants

class Item:
    def __init__(self, image_path):
        #self.game = game
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (25, -5) # montar random no primeiro 25 (x) pra definir a altura de x
        self.speed = 3

    def move(self):
        self.rect.y += self.speed
        self.rect.x = max(0, min(Constants.SCREEN_WIDTH - self.rect.width, self.rect.x))

    def blit(self, surface):
        surface.blit(self.image, self.rect.topleft)