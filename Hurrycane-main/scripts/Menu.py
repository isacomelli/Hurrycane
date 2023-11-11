import pygame, os
from pygame.locals import *
import Constants

class Menu:
    def __init__(self, sceneManager):
        self.sceneManager = sceneManager
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\menu_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.font = f"{os.path.abspath('.')}\\{Constants.GAME_FONT}"
        self.music = pygame.mixer.Sound(Constants.MENU_MUSIC)
        self.click_sound = pygame.mixer.Sound(Constants.MENU_CLICK_SOUND)
        self.select_sound = pygame.mixer.Sound(Constants.MENU_SELECT_SOUND)
        self.music.set_volume(0.30)

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
        selected = 0
        self.music.play()
        while display_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_UP:
                        self.select_sound.play() 
                        if selected == 0:
                            selected = 0   
                        else:
                            selected -= 1
                    elif event.key == pygame.K_DOWN:
                        self.select_sound.play() 
                        if selected == 2:
                            selected = 2 
                        else:
                            selected += 1 
                    if event.key==pygame.K_SPACE:
                        self.click_sound.play() 
                        if selected == 0:
                            self.sceneManager.set_state('characterMenu')
                            display_menu = False
                        if selected == 1:
                            self.sceneManager.set_state('rankingMenu')
                            display_menu = False
                        if selected == 2:
                            pygame.quit()
                            quit()

            # Main Menu UI
            # self.screen.fill(Constants.GRAY)
            self.screen.blit(self.background, (0, 0))

            if selected == 0:
                text_colors = [Constants.WHITE, Constants.BLACK, Constants.BLACK]
            elif selected == 1:
                text_colors = [Constants.BLACK, Constants.WHITE, Constants.BLACK]
            elif selected == 2:
                text_colors = [Constants.BLACK, Constants.BLACK, Constants.WHITE]

            title_text, shadow_title_text = self.text_format(Constants.GAME_NAME, Constants.YELLOW, text_size=70)
            start_text, shadow_start_text = self.text_format('START', text_colors[0])
            ranking_text, shadow_ranking_text = self.text_format('RANKING', text_colors[1])
            quit_text, shadow_quit_text = self.text_format('QUIT', text_colors[2])

            # Main Menu Text
            self.blit_text(shadow_title_text, y=80, is_shadow=True)
            self.blit_text(title_text, y=80)
            self.blit_text(shadow_start_text, y=300, is_shadow=True)
            self.blit_text(start_text, y=300)
            self.blit_text(shadow_ranking_text, y=360, is_shadow=True)
            self.blit_text(ranking_text, y=360)
            self.blit_text(shadow_quit_text, y=420, is_shadow=True)
            self.blit_text(quit_text, y=420)

            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)
        self.music.fadeout(5000)
            