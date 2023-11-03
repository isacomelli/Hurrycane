import pygame
import Level, Constants

class StreetTwo(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        pygame.display.set_caption("Hurrycane")
        self.background = pygame.image.load("img\\street2_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background_y = 0
        self.background_scroll_speed = 6

    def run(self):
        while True: # 5 segundos
            self.default_setups()

            if self.time > 4999:
                # self.sceneManager.set_state('menu')
                break