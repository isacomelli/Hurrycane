import pygame
import Constants, Score, RankingMenu
from pygame.locals import *
import os

class WinnerScreen:
    def __init__(self, sceneManager, score, game, ranking):
        pygame.font.init() 
        self.game = game
        self.sceneManager = sceneManager
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.font = f"{os.path.abspath('.')}\\{Constants.GAME_FONT}"
        self.score_object = score
        self.menuSound = pygame.mixer.Sound(Constants.MENU_RETURN_SOUND)
        self.menuWalk = pygame.mixer.Sound(Constants.MENU_WALK_SOUND)
        self.winnerMusic = pygame.mixer.Sound(Constants.WINNER_MUSIC)
        self.ranking = ranking

    # Text Renderer
    def text_format(self, message, text_color, text_size=30):
        new_font = pygame.font.Font(self.font, text_size)
        text = new_font.render(message, 1, text_color)
        return text
    
    def run(self):
        winnerScreen = True
        self.winnerMusic.play()
        selected = 0
        self.screen.fill(Constants.GRAY)

        # Texts
        select_text = self.text_format("Voce venceu!", (255, 255, 0), text_size=25)
        character1_name = self.text_format(f"PONTUACAO: {self.score_object.get_score()}", (255, 255, 255), text_size=30)

        # Text positioning
        text_rect = select_text.get_rect(center=(self.screen.get_width() // 2, 100))
        text_character1 = select_text.get_rect(center=(200, 280))

        # Display texts
        self.screen.blit(select_text, text_rect)
        self.screen.blit(character1_name, text_character1)
        pygame.display.flip()

        while winnerScreen:
            if self.ranking.lowest_score() < self.score_object.get_score():
                self.sceneManager.set_state('rankingMenu')
                winnerScreen = False
            else:    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.menuWalk.play() 
                            if selected == 0:
                                selected = 0   
                            else:
                                selected -= 1
                        elif event.key == pygame.K_DOWN:
                            self.menuWalk.play() 
                            if selected == 1:
                                selected = 1 
                            else:
                                selected += 1 
                        if event.key == pygame.K_RETURN:
                            self.menuSound.play()
                            if selected == 0:
                                self.sceneManager.set_state('rankingMenu')
                                winnerScreen = False
                            elif selected == 1:
                                self.sceneManager.set_state('menu')
                                winnerScreen = False
            
            if selected == 0:
                text_colors = [Constants.WHITE, Constants.BLACK]
            elif selected == 1:
                text_colors = [Constants.BLACK, Constants.WHITE]

            raking_text = self.text_format('RANKING', text_colors[0])
            raking_rect = raking_text.get_rect()
            self.screen.blit(raking_text, (Constants.SCREEN_WIDTH / 2 - (raking_rect[2] / 2), 500))

            return_text = self.text_format('MENU', text_colors[1])
            return_rect = return_text.get_rect()
            self.screen.blit(return_text, (Constants.SCREEN_WIDTH / 2 - (return_rect[2] / 2), 550))

            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)

        self.winnerMusic.stop()