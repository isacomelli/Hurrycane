import pygame
import sys
import Level, Constants

class StreetTwo(Level.Level):
    def __init__(self, game):
        super().__init__(game)
        # self.sceneManager.set_state('streetTwo')
        pygame.display.set_caption("Hurrycane")
        self.background = pygame.image.load("img\\teste_fundo3.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background_y = 0
        self.background_scroll_speed = 6

    def run(self):
        while self.time < 5000: # 5 segundos
            self.default_setups()