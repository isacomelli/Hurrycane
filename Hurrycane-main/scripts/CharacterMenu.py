import pygame
import Constants
from pygame.locals import *
import os

class CharacterMenu:
    def __init__(self, sceneManager):
        pygame.font.init() 
        self.sceneManager = sceneManager
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.font = f"{os.path.abspath('.')}\\{Constants.GAME_FONT}"
        self.character = None
        self.character1 = pygame.image.load(f"{os.path.abspath('.')}\\img\\ariel_running_1.png")
        self.character2 = pygame.image.load(f"{os.path.abspath('.')}\\img\\eric_running_1.png")
        self.selected = 0
        self.menuWalk = pygame.mixer.Sound(Constants.MENU_WALK_SOUND)
        self.menuSound = pygame.mixer.Sound(Constants.MENU_RETURN_SOUND)
        self.menuMusic = pygame.mixer.Sound(Constants.MENU_MUSIC)
        # self.run()

    # Text Renderer
    def text_format(self, message, text_color, text_size=75):
        new_font = pygame.font.Font(self.font, text_size)
        text = new_font.render(message, 1, text_color)
        return text

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def update_screen(self):
        self.menuWalk.play()
        self.screen.fill((90, 90, 90))
        if self.selected == 0:
            pygame.draw.rect(self.screen, (255, 255, 255), (80, 180, 130, 200), 4)
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), (280, 180, 130, 200), 4)

        #Mostra personagens + disposicao
        self.screen.blit(self.character1, (100, 200))
        self.screen.blit(self.character2, (300, 200))

        #textos
        select_text = self.text_format("Selecione seu personagem", (255, 255, 0), text_size=25)
        character1_name = self.text_format("Ariel",(255, 255, 255), text_size=23)
        character2_name = self.text_format("Eric",(255, 255, 255), text_size=23)

        #disposicao textos
        text_rect = select_text.get_rect(center=(self.screen.get_width() // 2, 100))
        text_character1= select_text.get_rect(center=(317, 350))
        text_character2 = select_text.get_rect(center=(505, 350))

        #exibe textos
        self.screen.blit(select_text, text_rect)
        self.screen.blit(character1_name, text_character1)
        self.screen.blit(character2_name, text_character2)
        pygame.display.flip()

    def run(self):
        characterMenu = True
        self.update_screen()

        while characterMenu:
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
                    if event.key == pygame.K_RETURN:
                        self.menuSound.play()
                        if self.selected == 0:
                            self.set_character('ariel')
                            self.sceneManager.set_state('streetOne')
                            characterMenu = False
                        if self.selected == 1:
                            self.set_character('eric')
                            self.sceneManager.set_state('streetOne')
                            characterMenu = False

            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)

        self.menuMusic.stop()
