import pygame
import Constants

class Score:
    score = 0
    def regular_score(self):
        self.score = self.score + 0.1

    def update_score(self, item_score):
        self.score += item_score

    def get_score_render(self):
        font = pygame.font.SysFont('..\\Retro.ttf', 40)
        score_text = f'SCORE: {int(self.score)}'
        score_render = font.render(score_text, True, Constants.GREEN) # (255, 0, 251) rosa
        # self.game.screen.blit(score_render, (10, 10))
        return score_render