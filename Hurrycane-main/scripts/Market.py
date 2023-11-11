import pygame, os
import Level, Constants

class Market(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        self.level_speed = Constants.LEVEL_SPEED * 2
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\market_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.marketMusic = pygame.mixer.Sound(Constants.MARKET_MUSIC)
        self.marketMusic.set_volume(0.3)

        self.item_json = {
            1: {
                'name': 'teste_item_market_1',
                'type': 'good',
                'speed': self.level_speed,
                'score': 1000,
                'size': (25, 25)
            },
            2: {
                'name': 'teste_item_market_2',
                'type': 'bad',
                'speed': self.level_speed,
                'score': -1000,
                'size': (50, 50)
            }
            # 1: {
            #     'name': 'water',
            #     'type': 'good',
            #     'speed': self.level_speed,
            #     'score': 1000,
            #     'size': (25, 25)
            # },
            # 2: {
            #     'name': 'food',
            #     'type': 'good',
            #     'speed': self.level_speed,
            #     'score': 1000,
            #     'size': (25, 25)
            # },
            # 3: {
            #     'name': 'med_kit',
            #     'type': 'good',
            #     'speed': self.level_speed,
            #     'score': 1000,
            #     'size': (25, 25)
            # },
            # 4: {
            #     'name': 'alcool',
            #     'type': 'bad',
            #     'speed': self.level_speed,
            #     'score': -1000,
            #     'size': (50, 50)
            # },
            # 5: {
            #     'name': 'cigarette',
            #     'type': 'bad',
            #     'speed': self.level_speed,
            #     'score': -1000,
            #     'size': (50, 50)
            # },
            # 6: {
            #     'name': 'videogame',
            #     'type': 'bad',
            #     'speed': self.level_speed,
            #     'score': -1000,
            #     'size': (50, 50)
            # }
        }

    def run(self):
        self.time = 0
        self.marketMusic.play()
        while True:
            # print(self.time)
            self.default_setups()

            # if self.time >= 40000:
            if self.time >= 10000:
                self.sceneManager.set_state('streetTwo')
                self.marketMusic.stop()
                break