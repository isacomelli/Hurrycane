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

        self.items = {item: attributes for item, attributes in game.items.items() if item in ['radio', 'water', 'food', 'city_hole', 'black_car', 'purple_car', 'green_car']}
        self.items = {item: {**attributes, 'speed': self.level_speed} for item, attributes in self.items.items()}
    
    def run(self):
        self.streetOneMusic.play()
        self.time = 0
        while True:
            self.default_setups()

            # print(self.time)
            if self.time >= 1000:
                self.sceneManager.set_state('market')
                self.streetOneMusic.stop()
                break