import pygame, os
from pygame.locals import *
import Constants, Hurrycane

class Menu:
    def __init__(self, game):
        self.game = game
        self.sceneManager = game.sceneManager
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\menu_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.logo = pygame.image.load(f"{os.path.abspath('.')}\\img\\logo.png")
        self.logo = pygame.transform.scale(self.logo, (346 * 1.2, 56 * 1.2))
        self.font = f"{os.path.abspath('.')}\\{Constants.GAME_FONT}"
        self.music = pygame.mixer.Sound(Constants.MENU_MUSIC)
        self.click_sound = pygame.mixer.Sound(Constants.MENU_CLICK_SOUND)
        self.select_sound = pygame.mixer.Sound(Constants.MENU_SELECT_SOUND)
        self.music.set_volume(0.30)
        self.hurrycane = Hurrycane.Hurrycane()
        self.hurrycane.size = (200, 200)
        self.hurrycane.position = (250, 140)

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

        if self.game.sound_on:
            self.music.play()
        
        while display_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_UP:
                        if self.game.sound_on:
                            self.select_sound.play() 
                        if selected == 0:
                            selected = 0   
                        else:
                            selected -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.game.sound_on:
                            self.select_sound.play() 
                        if selected == 3:
                            selected = 3 
                        else:
                            selected += 1 
                    if event.key==pygame.K_SPACE:
                        if self.game.sound_on:
                            self.click_sound.play() 
                        if selected == 0:
                            self.sceneManager.set_state('controlsScreen')
                            display_menu = False
                        if selected == 1:
                            self.sceneManager.set_state('rankingMenu')
                            display_menu = False
                        if selected == 2:
                            self.game.sound_on = not self.game.sound_on
                            if self.game.sound_on:
                                self.music.play()
                            else:
                                self.music.fadeout(1000)
                        if selected == 3:
                            pygame.quit()
                            quit()

            self.screen.blit(self.background, (0, 0))
            self.blit_text(self.logo, y=80)

            self.hurrycane.move()
            self.hurrycane.blit(self.screen)

            if selected == 0:
                text_colors = [Constants.WHITE, Constants.BLUE, Constants.BLUE, Constants.BLUE]
            elif selected == 1:
                text_colors = [Constants.BLUE, Constants.WHITE, Constants.BLUE, Constants.BLUE]
            elif selected == 2:
                text_colors = [Constants.BLUE, Constants.BLUE, Constants.WHITE, Constants.BLUE]
            elif selected == 3:
                text_colors = [Constants.BLUE, Constants.BLUE, Constants.BLUE, Constants.WHITE]

            start_text, shadow_start_text = self.text_format('START', text_colors[0])
            ranking_text, shadow_ranking_text = self.text_format('RANKING', text_colors[1])
            sound_text, shadow_sound_text = self.text_format(f"SOUND: {'ON' if self.game.sound_on else 'OFF'}", text_colors[2])
            quit_text, shadow_quit_text = self.text_format('QUIT', text_colors[3])

            self.blit_text(shadow_start_text, y=300, is_shadow=True)
            self.blit_text(start_text, y=300)
            self.blit_text(shadow_ranking_text, y=360, is_shadow=True)
            self.blit_text(ranking_text, y=360)
            self.blit_text(shadow_sound_text, y=420, is_shadow=True)
            self.blit_text(sound_text, y=420)
            self.blit_text(shadow_quit_text, y=480, is_shadow=True)
            self.blit_text(quit_text, y=480)

            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)

        self.music.fadeout(1000)    