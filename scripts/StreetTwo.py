import pygame, os
import Level, Constants

class StreetTwo(Level.Level):
    def __init__(self, game, sceneManager):
        super().__init__(game, sceneManager)
        self.level_speed = Constants.LEVEL_SPEED * 2.5
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\streetTwo_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.streetTwoMusic = pygame.mixer.Sound(Constants.STREETTWO_MUSIC)

        self.items = {item: attributes for item, attributes in game.items.items() if item in ['radio', 'lantern', 'water', 'med_kit', 'forest_hole', 'cigarette', 'purple_car', 'red_car']}
        self.items = {item: {**attributes, 'speed': self.level_speed} for item, attributes in self.items.items()}

    def run(self):
        self.time = 0
        self.streetTwoMusic.play()
        while True:
            self.default_setups()

            # if self.time >= 70000:
            if self.time >= 3000:
                self.sceneManager.set_state('winnerScreen')
                self.streetTwoMusic.stop()
                break