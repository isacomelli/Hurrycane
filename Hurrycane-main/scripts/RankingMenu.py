import pygame
import Constants
from pygame.locals import *
import os

class RankingMenu:
    def __init__(self, sceneManager, score):
        self.sceneManager = sceneManager
        self.score_object = score
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.font = f"{os.path.abspath('.')}\\{Constants.GAME_FONT}"
        self.menuSound = pygame.mixer.Sound(Constants.MENU_RETURN_SOUND)
        self.newRecord = False

    
    # Function to read the file and create a list of tuples (name, score)
    def get_ranking(self):
        ranking = []
        with open('Ranking.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, score = line.strip().split(';')
                ranking.append((name, int(score)))

        ranking.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return ranking

    def lowest_score(self):
        numbers = [number for _, number in self.get_ranking()]
        lowest_number = min(numbers)
        return lowest_number
    
    def verify_record(self, score):
        if self.lowest_score() < score:
            return True

    # Text Renderer
    def text_format(self, message, text_color, text_size=40):
        new_font = pygame.font.Font(self.font, text_size)
        text = new_font.render(message, 0, text_color)
        return text

    
    def run(self):
        ranking_menu = True
        selected = 0

        while self.verify_record(self.score_object.get_score()):
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_UP:
                       if selected == 0:
                           selected = 0
                   if event.key==pygame.K_RETURN:
                       self.menuSound.play()
                       if selected == 0:
                           return
  
            # Main Menu UI
            self.screen.fill(Constants.GREEN)

            title = self.text_format('NOVO RECORDE', Constants.YELLOW, text_size=60)            
            title_rect = title.get_rect()
            self.screen.blit(title, (Constants.SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
            
            return_text = self.text_format('PROXIMO', Constants.WHITE)
            return_rect = return_text.get_rect()
            self.screen.blit(return_text, (Constants.SCREEN_WIDTH / 2 - (return_rect[2] / 2), 550))

            character1_name = self.text_format(f"PONTUACAO: {self.score_object.get_score()}", (255, 255, 255), text_size=30)
            text_character1 = character1_name.get_rect(center=(200, 330))
            self.screen.blit(character1_name, text_character1)            
            
            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)

        while ranking_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if selected == 0:
                            selected = 0
                    if event.key==pygame.K_RETURN:
                        # START, RANKING e QUIT
                        self.menuSound.play()
                        if selected == 0:
                            self.sceneManager.set_state('menu')
                            ranking_menu = False
                            # print('return')

            # Main Menu UI
            self.screen.fill(Constants.GRAY)

            title = self.text_format('RANKING', Constants.YELLOW, text_size=90)            
            title_rect = title.get_rect()
            self.screen.blit(title, (Constants.SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
            
            return_text = self.text_format('RETURN', Constants.WHITE)
            return_rect = return_text.get_rect()
            self.screen.blit(return_text, (Constants.SCREEN_WIDTH / 2 - (return_rect[2] / 2), 550))

            # Read the file and create the ranking
            ranking = self.get_ranking()

            ranking_start_position = 200
            for place, (name, score) in enumerate(ranking[:5]):
                text = self.text_format(f"{place + 1}. {name.upper()} - {score}", Constants.BLACK)
                rect = text.get_rect()

                self.screen.blit(text, (80, ranking_start_position))
                ranking_start_position += 60

            
            pygame.display.update()
            pygame.display.set_caption(Constants.GAME_NAME)
            