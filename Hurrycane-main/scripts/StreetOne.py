import pygame
import sys
import Level, Constants

class StreetOne(Level.Level):
    def __init__(self, game):
        super().__init__(game)
        # self.sceneManager.set_state('streetOne')
        pygame.display.set_caption("Hurrycane")
        self.background = pygame.image.load("img\\street1_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background_y = 0
        self.background_scroll_speed = 2
    
    def run(self):
        while self.time < 30000: # 30 segundos
            self.default_setups()