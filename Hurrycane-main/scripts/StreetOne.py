import pygame
import Level, Constants,Menu
import os

class StreetOne(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        self.level_speed = Constants.LEVEL_SPEED
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\streetOne_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.streetOneMusic = pygame.mixer.Sound(Constants.STREETONE_MUSIC)
        self.streetOneMusic.set_volume(0.30)

        self.item_json = {
            1: {
                'name': 'teste_item_streetOne_1',
                'type': 'good',
                'speed': self.level_speed,
                'score': 500,
                'size': (25, 25)
            },
            2: {
                'name': 'teste_item_streetOne_2',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -500,
                'size': (50, 50)
            }
        }
    
    def run(self):
        self.streetOneMusic.play()
        self.time = 0
        while True:
            self.default_setups()

            if self.time > 3000: # 10 segundos
                self.sceneManager.set_state('market')
                break
        self.streetOneMusic.stop()