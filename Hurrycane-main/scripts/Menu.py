import pygame
import Constants
from pygame.locals import *


class Menu:
    def __init__(self, sceneManager):
        self.sceneManager = sceneManager
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.font = '..\\Retro.ttf'
        self.run()

    # Text Renderer
    def text_format(self, message, text_color, text_size=75):
        new_font = pygame.font.Font(self.font, text_size)
        text = new_font.render(message, 0, text_color)
        return text
    
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
                        if selected == 2:
                            selected = 2 
                        else:
                            selected += 1
                    if event.key==pygame.K_RETURN:
                        # START, RANKING e QUIT
                        if selected == 0:
                            self.sceneManager.set_state('streetOne')
                            menu = False
                            print('START')
                        if selected == 1:
                            print('RANKING')
                        if selected == 2:
                            print('QUIT')
                            pygame.quit()
                            quit()

            # Main Menu UI
            self.screen.fill(Constants.GRAY)

            if selected == 0:
                text_colors = [Constants.WHITE, Constants.BLACK, Constants.BLACK]
            elif selected == 1:
                text_colors = [Constants.BLACK, Constants.WHITE, Constants.BLACK]
            elif selected == 2:
                text_colors = [Constants.BLACK, Constants.BLACK, Constants.WHITE]

            title = self.text_format(Constants.GAME_NAME, Constants.YELLOW, text_size=90)
            text_start = self.text_format('START', text_colors[0])
            text_ranking = self.text_format('RANKING', text_colors[1])
            text_quit = self.text_format('QUIT', text_colors[2])

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            ranking_rect = text_ranking.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            self.screen.blit(title, (Constants.SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
            self.screen.blit(text_start, (Constants.SCREEN_WIDTH / 2 - (start_rect[2] / 2), 300))
            self.screen.blit(text_ranking, (Constants.SCREEN_WIDTH / 2 - (ranking_rect[2] / 2), 360))
            self.screen.blit(text_quit, (Constants.SCREEN_WIDTH / 2 - (quit_rect[2] / 2), 420))

            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)
            