import pygame
import Level, Constants
import os

class StreetTwo(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        self.level_speed = Constants.LEVEL_SPEED
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\streetTwo_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.streetTwoMusic = pygame.mixer.Sound(Constants.STREETTWO_MUSIC)

        self.item_json = {
            1: {
                'name': 'teste_item_streetTwo_1',
                'type': 'good',
                'speed': self.level_speed,
                'score': 5000,
                'size': (25, 25)
            },
            2: {
                'name': 'teste_item_streetTwo_2',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -5000,
                'size': (25, 25)
            }
        }

    def run(self):
        self.time = 0
        self.streetTwoMusic.play()
        while True:
            self.default_setups()

            if self.time > 5000:
                self.sceneManager.set_state('winnerScreen')
                break
        self.streetTwoMusic.stop()