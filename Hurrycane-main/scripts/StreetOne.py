import pygame, os
import Level, Constants

class StreetOne(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        self.level_speed = Constants.LEVEL_SPEED
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\streetOne_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.streetOneMusic = pygame.mixer.Sound(Constants.STREETONE_MUSIC)
        self.streetOneMusic.set_volume(0.30)

        self.item_json = {
            #1: {
            #    'name': 'teste_item_streetOne_1',
            #    'type': 'good',
            #    'speed': self.level_speed,
            #    'score': 500,
            #    'size': (25, 25)
            #},
            #2: {
            #    'name': 'teste_item_streetOne_2',
            #    'type': 'bad',
            #    'speed': self.level_speed,
            #    'score': -500,
            #    'size': (50, 50)
            
            1: {
                'name': 'radio',
                'type': 'good',
                'speed': self.level_speed,
                'score': 500,
                'size': (40, 44) #proporcao 1.10
            },
            2: {
                'name': 'water',
                'type': 'good',
                'speed': self.level_speed,
                'score': 500,
                'size': (30, 90) #proporcao = 3
            },
            3: {
                'name': 'city_hole',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -500,
                'size': (60, 20) #proporcao = 1.8
            },
            4: {
                'name': 'black_car',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -500,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT) #proporcao = 2.20
            },
            5: {
                'name': 'purple_car',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -500,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT)
            },
            6: {
                'name': 'red_car',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -500,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT)
            },
            7: {
                'name': 'gray_car',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -500,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT)
            },
            8: {
                'name': 'green_car',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -500,
                'size': (Constants.CAR_WIDTH, Constants.CAR_HEIGHT)
            }
        }
    
    def run(self):
        self.streetOneMusic.play()
        self.time = 0
        while True:
            self.default_setups()

            # print(self.time)
            if self.time >= 5000: # 10 segundos
                self.sceneManager.set_state('market')
                self.streetOneMusic.stop()
                break