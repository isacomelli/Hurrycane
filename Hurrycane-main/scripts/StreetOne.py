import pygame, os
import Level, Constants

class StreetOne(Level.Level):
    def __init__(self, game):
        super().__init__(game)
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\streetOne_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.streetOne_music = pygame.mixer.Sound(Constants.STREETONE_MUSIC)
        self.streetOne_music.set_volume(0.30)
        self.multiplier = 1
        self.level_speed = Constants.LEVEL_SPEED * self.multiplier

        self.items = {item: attributes for item, attributes in game.items.items() if item in ['radio', 'water', 'food', 'city_hole', 'black_car', 'purple_car', 'green_car']}
        self.items = {item: {**attributes, 'speed': self.level_speed} for item, attributes in self.items.items()}
    
    def run(self):
        self.time = 0
        if self.game.sound_on:
            self.streetOne_music.play()

        while True:
            self.default_setups()

            if self.time >= 30000:
                self.sceneManager.set_state('market')
                break
            elif self.game.player.lives == 0:
                self.sceneManager.set_state('defeatScreen')
                break

        self.streetOne_music.stop()