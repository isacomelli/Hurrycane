import pygame
import Constants
from pygame.locals import *


class Menu:
    def __init__(self, sceneManager):
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.font = 'Retro.ttf'
        self.sceneManager = sceneManager
        self.run()

    # Text Renderer
    def text_format(self, message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)
        return newText
    
    def run(self):
        menu = True
        selected = 0
    
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if selected == 0:
                            selected = 0
                        else:
                            selected -= 1
                    elif event.key == pygame.K_DOWN:
                        if selected == 4:
                            selected = 4
                        else:
                            selected += 1
                    if event.key==pygame.K_RETURN:
                        #TITLE, START, CHARACTER, OPTION, ABOUT
                        if selected == 0:
                            menu = False
                            self.sceneManager.set_state('streetOne')
                            print('Start')
                        if selected == 1:
                            print('character')
                        if selected == 2:
                            print('option')
                        if selected == 3:
                            print('about')
                        if selected == 4:
                            pygame.quit()
                            quit()

    
            # Main Menu UI
            self.screen.fill(Constants.GRAY)
            title = self.text_format('HurryCane', self.font, 90, Constants.YELLOW)
            if selected == 0:
                text_start = self.text_format('START', self.font, 75, Constants.WHITE)
            else:
                text_start = self.text_format('START', self.font, 75, Constants.BLACK)
            if selected == 1:
                text_character = self.text_format('CHARACTER', self.font, 75, Constants.WHITE)
            else:
                text_character = self.text_format('CHARACTER', self.font, 75, Constants.BLACK)
            if selected == 2:
                text_options = self.text_format('OPTIONS', self.font, 75, Constants.WHITE)
            else:
                text_options = self.text_format('OPTIONS', self.font, 75, Constants.BLACK)
            if selected == 3:
                text_about = self.text_format('ABOUT', self.font, 75, Constants.WHITE)
            else:
                text_about = self.text_format('ABOUT', self.font, 75, Constants.BLACK)
            if selected == 4:
                text_quit = self.text_format('QUIT', self.font, 75, Constants.WHITE)
            else:
                text_quit = self.text_format('QUIT', self.font, 75, Constants.BLACK)
    
            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            character_rect = text_character.get_rect()
            options_rect = text_options.get_rect()
            about_rect = text_about.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            self.screen.blit(title, (Constants.SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
            self.screen.blit(text_start, (Constants.SCREEN_WIDTH / 2 - (start_rect[2] / 2), 300))
            self.screen.blit(text_character, (Constants.SCREEN_WIDTH / 2 - (character_rect[2] / 2), 360))
            self.screen.blit(text_options, (Constants.SCREEN_WIDTH / 2 - (options_rect[2] / 2), 420))
            self.screen.blit(text_about, (Constants.SCREEN_WIDTH / 2 - (about_rect[2] / 2), 480))
            self.screen.blit(text_quit, (Constants.SCREEN_WIDTH / 2 - (quit_rect[2] / 2), 540))

            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)
            
