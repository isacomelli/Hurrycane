import pygame
import sys
import Level, Constants

class Market(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        self.level_speed = 4
        self.background = pygame.image.load("img\\market_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

        self.item_json = {
            1: {
                'name': 'teste_item_market_1',
                'type': 'good',
                'speed': self.level_speed,
                'score': 1000
            },
            2: {
                'name': 'teste_item_market_2',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -1000
            }
        }

    def run(self):
        self.time = 0
        while True:
            # print(self.time)
            self.default_setups()

            if self.time > 4999:
                self.sceneManager.set_state('streetTwo')
                break