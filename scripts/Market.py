import pygame
import sys
import Level, Constants

class Market(Level.Level):
    def __init__(self, game):
        super().__init__(game)
        # self.sceneManager.set_state('market')
        pygame.display.set_caption("Hurrycane")
        self.background = pygame.image.load("img\\teste_fundo2.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background_y = 0
        self.background_scroll_speed = 2

    def run(self):
        while self.game.score.score < 40:
            self.default_setups()