import pygame, os
import Level, Constants

class Market(Level.Level):
    def __init__(self, game):
        super().__init__(game)
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\market_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.market_music = pygame.mixer.Sound(Constants.MARKET_MUSIC)
        self.market_music.set_volume(0.3)
        self.multiplier = 2
        self.level_speed = Constants.LEVEL_SPEED * self.multiplier

        self.items = {item: attributes for item, attributes in game.items.items() if item in ['radio', 'water', 'food', 'med_kit', 'alcool', 'videogame', 'cigarette', 'market_cart']}
        self.items = {item: {**attributes, 'speed': self.level_speed} for item, attributes in self.items.items()}

    def run(self):
        self.time = 0
        if self.game.sound_on:
            self.market_music.play()

        while True:
            self.default_setups()

            if self.time >= 60000:
                self.sceneManager.set_state('streetTwo')
                break
            elif self.game.player.lives == 0:
                self.sceneManager.set_state('defeatScreen')
                break

        self.market_music.stop()