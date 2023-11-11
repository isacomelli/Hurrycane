import pygame, sys, os, random
import Constants 

class Item:
    def __init__(self, item_json):
        self.name = item_json['name']
        self.type = item_json['type']
        self.speed = item_json['speed']
        self.score = item_json['score']
        self_size = item_json['size']

       

        self.image = pygame.image.load(f"{os.path.abspath('.')}\\img\\{item_json['name']}.png")
        self.image = pygame.transform.scale(self.image, self_size)
        self.rect = self.image.get_rect()
        half_width = self.rect.width // 2
        min_x = max(Constants.PLAYER_LANE_MIN_X + half_width - 3, Constants.PLAYER_LANE_MIN_X)
        max_x = min(Constants.PLAYER_LANE_MAX_X + self.rect.width + 3, Constants.PLAYER_LANE_MAX_X)
        self.rect.center = (random.randint(min_x, max_x), -5) 


    def move(self):
        self.rect.y += self.speed
        self.rect.x = max(0, min(Constants.SCREEN_WIDTH - self.rect.width, self.rect.x))

    def blit(self, surface):
        surface.blit(self.image, self.rect.topleft)