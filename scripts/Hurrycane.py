import pygame
import Constants

class Hurrycane:
    def __init__(self):
        self.running_images = [pygame.image.load(f'img\\hurrycane_{x}.png') for x in range(1, 19)]
        self.current_image_number = 0
        self.image = None
        self.size = (1000, 1000)
        self.position = (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT * 1.55)

    def move(self): 
        self.image = self.running_images[self.current_image_number]
        self.current_image_number = (self.current_image_number + 1) % len(self.running_images)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def blit(self, surface):
        surface.blit(self.image, self.rect.topleft)