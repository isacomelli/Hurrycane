import pygame
import Level, Constants

class StreetOne(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        self.level_speed = 2
        self.background = pygame.image.load("img\\streetOne_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

        self.item_json = {
            1: {
                'name': 'teste_item_streetOne_1',
                'type': 'good',
                'speed': self.level_speed,
                'score': 500
            },
            2: {
                'name': 'teste_item_streetOne_2',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -500
            }
        }
    
    def run(self):
        self.time = 0
        while True:
            self.default_setups()

            if self.time > 14999: # 10 segundos
                self.sceneManager.set_state('market')
                break