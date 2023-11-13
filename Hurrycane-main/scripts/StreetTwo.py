import pygame, os
import Level, Constants

class StreetTwo(Level.Level):
    def __init__(self, game):
        super().__init__(game)
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\streetTwo_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.streetTwo_music = pygame.mixer.Sound(Constants.STREETTWO_MUSIC)
        self.multiplier = 2.5
        self.level_speed = Constants.LEVEL_SPEED * self.multiplier

        self.items = {item: attributes for item, attributes in game.items.items() if item in ['radio', 'lantern', 'water', 'med_kit', 'forest_hole', 'cigarette', 'purple_car', 'red_car']}
        self.items = {item: {**attributes, 'speed': self.level_speed} for item, attributes in self.items.items()}

    def run(self):
        self.time = 0
        if self.game.sound_on:
            self.streetTwo_music.play()
        
        while True:
            self.default_setups()

            if self.time >= 90000:
                self.sceneManager.set_state('winnerScreen')
                break
            elif self.game.player.lives == 0:
                self.sceneManager.set_state('defeatScreen')
                break

        self.streetTwo_music.stop()