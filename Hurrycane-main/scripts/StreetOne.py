import pygame
import Level, Constants

class StreetOne(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        pygame.display.set_caption("Hurrycane")
        self.background = pygame.image.load("img\\street1_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background_y = 0
        self.background_scroll_speed = 2
    
    def run(self):
        while True:
            self.default_setups()

            if self.time > 9999: # 10 segundos
                self.sceneManager.set_state('market')
                break