import pygame, os
import Constants

class Score:
    score = 0
    def regular_score(self):
        self.score += 0.1

    def update_score(self, item_score):
        self.score += item_score

    def get_score_render(self):
        font = pygame.font.SysFont(f"{os.path.abspath('.')}\\{Constants.GAME_FONT}", 40)
        score_text = f'SCORE: {int(self.score)}'
        score_render = font.render(score_text, True, Constants.GREEN) # (255, 0, 251) rosa
        shadow_score_render = font.render(score_text, True, Constants.BLACK) # (255, 0, 251) rosa
        return score_render, shadow_score_render
    
    def get_score(self):
        return int(self.score)