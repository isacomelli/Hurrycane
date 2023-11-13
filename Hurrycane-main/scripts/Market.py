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

        self.items = {item: attributes for item, attributes in game.items.items() if item in ['radio', 'water', 'food', 'med_kit', 'alcool', 'videogame', 'cigarette', 'market_cart']}
        self.items = {item: {**attributes, 'speed': self.level_speed} for item, attributes in self.items.items()}

    def run(self):
        self.time = 0
        self.marketMusic.play()
        while True:
            # print(self.time)
            self.default_setups()

            # if self.time >= 40000:
            if self.time >= 2000:
                self.sceneManager.set_state('streetTwo')
                self.marketMusic.stop()
                break