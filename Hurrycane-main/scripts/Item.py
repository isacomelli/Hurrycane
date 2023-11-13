import pygame, sys, os, random
import Constants 

class Item:
    def __init__(self, item_json, x):
        self.name = item_json['name']
        self.type = item_json['type']
        self.speed = item_json['speed']
        self.score = item_json['score']
        self_size = item_json['size']

        self.image = pygame.image.load(f"{os.path.abspath('.')}\\img\\{item_json['name']}.png")
        self.image = pygame.transform.scale(self.image, self_size)
        self.rect = self.image.get_rect()
        self.half_width = self.rect.width // 2
        self.min_x = max(Constants.PLAYER_LANE_MIN_X + self.half_width - 3, Constants.PLAYER_LANE_MIN_X)
        self.max_x = min(Constants.PLAYER_LANE_MAX_X + self.rect.width + 3, Constants.PLAYER_LANE_MAX_X)
        self.rect.center = self.set_rect_center(x)

    def set_rect_center(self, x):
        if x:
            return (x, Constants.CAR_HEIGHT * -1)
        return (random.randint(self.min_x, self.max_x), Constants.CAR_HEIGHT * -1)

    def move(self):
        self.rect.y += self.speed
        self.rect.x = max(0, min(Constants.SCREEN_WIDTH - self.rect.width, self.rect.x))

    def blit(self, surface):
        surface.blit(self.image, self.rect.topleft)