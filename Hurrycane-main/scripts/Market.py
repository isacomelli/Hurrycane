import pygame
import sys
import Level, Constants

class Market(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        pygame.display.set_caption("Hurrycane")
        self.background = pygame.image.load("img\\market_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background_y = 0
        self.background_scroll_speed = 4

    def run(self):
        while True:
            # print(self.time)
            self.default_setups()

            if self.time > 9999:
                self.sceneManager.set_state('streetTwo')
                break