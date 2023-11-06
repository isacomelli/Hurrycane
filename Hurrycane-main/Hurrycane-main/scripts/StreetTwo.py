import pygame
import Level, Constants

class StreetTwo(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        self.level_speed = 8
        self.background = pygame.image.load("img\\streetTwo_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

        self.item_json = {
            1: {
                'name': 'teste_item_streetTwo_1',
                'type': 'good',
                'speed': self.level_speed,
                'score': 5000
            },
            2: {
                'name': 'teste_item_streetTwo_2',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -5000
            }
        }

    def run(self):
        self.time = 0
        while True: # 5 segundos
            self.default_setups()

            if self.time > 4999:
                self.sceneManager.set_state('menu')
                break