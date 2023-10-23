import pygame
import sys
from scripts import Game, Level, Constants

class Level:
    def __init__(self, game):
        self.game = game
        self.player = game.player
    
    def run(self):
        pass

    def default_setups(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualizando a imagem do fundo
        self.background_y += self.background_scroll_speed
        self.game.screen.blit(self.background, (0, self.background_y))
        self.game.screen.blit(self.background, (0, self.background_y - Constants.SCREEN_HEIGHT))

        if self.background_y >= Constants.SCREEN_HEIGHT:
            self.background_y = 0

        # Movimento da sprite do jogador
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        self.player.blit(self.game.screen)

        #pontuacao
        self.game.score.regularScore()
        font = pygame.font.SysFont('sans', 40)
        score_text = f'SCORE: {int(self.game.score.score)}'
        scoreShow = font.render(score_text, True, (255, 0, 251))
        self.game.screen.blit(scoreShow, (10, 10))

        pygame.display.flip()
        self.game.clock.tick(60)