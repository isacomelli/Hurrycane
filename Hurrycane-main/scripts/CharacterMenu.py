import pygame, os
from pygame.locals import *
import Constants

class CharacterMenu:
    def __init__(self, game):
        self.game = game
        self.sceneManager = game.sceneManager
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.font = f"{os.path.abspath('.')}\\{Constants.GAME_FONT}"
        self.character = None
        self.ariel_image = pygame.image.load(f"{os.path.abspath('.')}\\img\\ariel_1.png")
        self.eric_image = pygame.image.load(f"{os.path.abspath('.')}\\img\\eric_1.png")
        self.selected = 0
        self.select_sound = pygame.mixer.Sound(Constants.MENU_SELECT_SOUND)
        self.click_sound = pygame.mixer.Sound(Constants.MENU_CLICK_SOUND)

    def text_format(self, message, text_color, text_size=30):
        new_font = pygame.font.Font(self.font, text_size)
        text = new_font.render(message, 0, text_color)
        shadow_text = new_font.render(message, 0, Constants.BLACK)
        return text, shadow_text

    def blit_text(self, text, x=0, y=0, is_shadow=False):
        rect = text.get_rect()
        
        if not x:
            x = (Constants.SCREEN_WIDTH / 2 - (rect[2] / 2))
        if is_shadow:
            x -= 3
            y -= 3

        self.screen.blit(text, (x, y))

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def update_screen(self):
        if self.game.sound_on:
            self.select_sound.play()
        self.screen.fill(Constants.DARK_BLUE)
        if self.selected == 0:
            pygame.draw.rect(self.screen, Constants.WHITE, (80, 180, 130, 220), 4)
        else:
            pygame.draw.rect(self.screen, Constants.WHITE, (280, 180, 130, 220), 4)

        self.screen.blit(self.ariel_image, (100, 200))
        self.screen.blit(self.eric_image, (300, 200))

        if self.selected == 0:
            text_colors = [Constants.WHITE, Constants.BLUE]
        else:
            text_colors = [Constants.BLUE, Constants.WHITE]

        select_text, shadow_select_text = self.text_format('CHOOSE YOUR CHARACTER', Constants.LIGHT_BLUE, text_size=28)
        ariel_text, shadow_ariel_text = self.text_format('Ariel', text_colors[0], text_size=25)
        eric_text, shadow_eric_text = self.text_format('Eric', text_colors[1], text_size=25)

        self.blit_text(shadow_select_text, y=100, is_shadow=True)
        self.blit_text(select_text, y=100)
        self.blit_text(shadow_ariel_text, x=110, y=350, is_shadow=True)
        self.blit_text(ariel_text, x=110, y=350)
        self.blit_text(shadow_eric_text, x=317, y=350, is_shadow=True)
        self.blit_text(eric_text, x=317, y=350)
        pygame.display.flip()

    def run(self):
        display_menu = True
        self.update_screen()

        while display_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.selected = 1 - self.selected
                        self.update_screen()
                    elif event.key == pygame.K_LEFT:
                        self.selected = 1 - self.selected
                        self.update_screen()
                    if event.key == pygame.K_SPACE:
                        if self.game.sound_on:
                            self.click_sound.play()
                        if self.selected == 0:
                            self.set_character('ariel')
                            self.sceneManager.set_state('streetOne')
                            display_menu = False
                        if self.selected == 1:
                            self.set_character('eric')
                            self.sceneManager.set_state('streetOne')
                            display_menu = False

            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)
