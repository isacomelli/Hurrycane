import pygame
import sys
import random
import Game, Level, Constants

class Item:
    def __init__(self, image_path):
        #self.game = game
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(Constants.PLAYER_LANE_MIN_X + self.rect.width // 2 - 3, Constants.PLAYER_LANE_MAX_X + self.rect.width * 2.28 + 3), -5) #

        self.speed = 6

    def move(self):
        self.rect.y += self.speed
        self.rect.x = max(0, min(Constants.SCREEN_WIDTH - self.rect.width, self.rect.x))

    def blit(self, surface):
        surface.blit(self.image, self.rect.topleft)