import pygame
import sys
import Level, Constants

class Market(Level.Level):
    def __init__(self, game):
        super().__init__(game)
        # self.sceneManager.set_state('market')
        pygame.display.set_caption("Hurrycane")
        self.background = pygame.image.load("img\\market_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background_y = 0
        self.background_scroll_speed = 4

    def run(self):
        while self.time < 10000: # 10 segundos
            print(self.time)
            self.default_setups()