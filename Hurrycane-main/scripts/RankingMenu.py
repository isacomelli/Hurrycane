import pygame, os
from pygame.locals import *
import Constants
from Ranking import Ranking

class RankingMenu:
    def __init__(self, sceneManager):
        self.sceneManager = sceneManager
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.font = f"{os.path.abspath('.')}\\{Constants.GAME_FONT}"
        self.click_sound = pygame.mixer.Sound(Constants.MENU_CLICK_SOUND)

    # Text Renderer
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
    
    def run(self):
        display_menu = True

        while display_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.click_sound.play()
                        self.sceneManager.set_state('menu')
                        display_menu = False
                            # print('return')

            if self.sceneManager.get_previous_state() == 'winningScreen':
                state_string = 'MENU'
            else:
                state_string = 'RETURN'

            # Main Menu UI
            self.screen.fill(Constants.GRAY)

            title_text, shadow_title_text = self.text_format('RANKING', Constants.YELLOW, text_size=70)            
            state_text, shadow_state_text = self.text_format(state_string, Constants.WHITE)

            self.blit_text(shadow_title_text, y=80, is_shadow=True)
            self.blit_text(title_text, y=80)
            
            self.blit_text(shadow_state_text, y=550, is_shadow=True)
            self.blit_text(state_text, y=550)

            # Read the file and create the ranking
            ranking = Ranking().ranking

            ranking_start_position = 200
            for place, (name, score) in enumerate(ranking[:5]):
                ranking_text, shadow_ranking_text = self.text_format(f"{place + 1}. {name.upper()} - {score}", Constants.WHITE)

                self.blit_text(shadow_ranking_text, x=130, y=ranking_start_position, is_shadow=True)
                self.blit_text(ranking_text, x=130, y=ranking_start_position)
                ranking_start_position += 60

            
            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)
            