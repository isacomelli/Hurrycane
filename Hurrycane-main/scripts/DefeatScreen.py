import pygame, os
from pygame.locals import *
import Constants
from Ranking import Ranking

class DefeatScreen:
    def __init__(self, game):
        self.game = game
        self.sceneManager = game.sceneManager
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background = pygame.image.load(f"{os.path.abspath('.')}\\img\\defeat_background.png")
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.font = f"{os.path.abspath('.')}\\{Constants.GAME_FONT}"
        self.final_score = game.score.get_score()
        self.ranking = Ranking()
        self.click_sound = pygame.mixer.Sound(Constants.MENU_CLICK_SOUND)
        self.music = pygame.mixer.Sound(Constants.DEFEAT_MUSIC)
        self.username = ''

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

    def verify_record(self):
        if self.final_score > self.ranking.get_fifth_highest_score():
            return True
        return False

    def run(self):
        display_screen = True
        if self.game.sound_on:
            self.music.play()

        if self.verify_record():
            title = 'GAME OVER! but.. NEW RECORD!'
            next_state = 'rankingMenu'
            state_string = 'NEXT'
        else:
            title = "GAME OVER!"
            next_state = 'menu'
            state_string = 'MENU'

        while display_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.game.sound_on:
                            self.click_sound.play()
                        if self.verify_record():
                            if len(self.username):
                                self.sceneManager.set_state(next_state)
                                display_screen = False
                        else:
                            self.sceneManager.set_state(next_state)
                            display_screen = False
                    
                    if self.verify_record():
                        if event.key == pygame.K_BACKSPACE:
                            self.username = self.username[:-1]
                        elif event.unicode != ' ' and len(self.username) < 4:
                            self.username += event.unicode

            self.screen.blit(self.background, (0, 0))

            if self.verify_record():
                title_text, shadow_title_text = self.text_format(' '.join(title.split()[:3]), Constants.YELLOW)
                title_text_2, shadow_title_text_2 = self.text_format(' '.join(title.split()[3:]), Constants.YELLOW)
            else:
                title_text, shadow_title_text = self.text_format(title, Constants.YELLOW)
            score_text, shadow_score_text = self.text_format(f'SCORE: {self.final_score}', Constants.YELLOW)
            input_text, shadow_input_text = self.text_format(f'NOME: {self.username}', Constants.YELLOW)
            state_text, shadow_state_text = self.text_format(state_string, Constants.WHITE)

            if self.verify_record():
                self.blit_text(shadow_title_text_2, y=120, is_shadow=True)
                self.blit_text(title_text_2, y=120)

            self.blit_text(shadow_title_text, y=80, is_shadow=True)
            self.blit_text(title_text, y=80)
            self.blit_text(shadow_score_text, y=280, is_shadow=True)
            self.blit_text(score_text, y=280)
            self.blit_text(shadow_state_text, y=550, is_shadow=True)
            self.blit_text(state_text, y=550)

            if self.verify_record():
                self.blit_text(shadow_input_text, x=147, y=397)
                self.blit_text(input_text, x=150, y=400)

            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)

        if self.verify_record():
            Ranking().write_ranking(self.username, self.final_score)
            
        self.music.stop()