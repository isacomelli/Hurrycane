# ISA - Comentários
# - Aqui o personagem tá fixo, mas depois de criar o menu, vai se tornar variável
# - prof passou nada de POO em python, mas:
#   - Constantes não precisam ir dentro de __init__, podem ir fora sem usar o self; acho aplicável para o tamanho da tela, mas tbm não é um problema ir ali
#   - Todos os atributos e métodos estão em public... não sei se seria um problema manter, mas acho q não

import pygame
import sys
from models import Player
from models import Score
from models import SceneManager

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen_width = 300
        self.screen_height = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Hurrycane")
        self.background = pygame.image.load("img\\teste_fundo.png")
        
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.background_y = 0
        self.background_scroll_speed = 1
        self.player = Player.Player(self, self.screen_width // 2, self.screen_height - 100, "img\\ariel.png")
        self.score = Score.Score()
        self.clock = pygame.time.Clock()

        #SCENE MANAGER
        #self.sceneManager = SceneManager('menu')
        #self.states = {
        #               'menu': self.menu, 
        #               'street1':self.street1, 
        #               'market': self.market, 
        #               'street2': self.street2, 
        #               'defeat': self.defeat, 
        #               'winner': self.winner
        #               }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #scene manager 
            #https://www.youtube.com/watch?v=r0ixaTQxsUI
            #self.states[self.sceneManager.get_state()].run()
            #self.sceneManager.set_state('street1')

            # Atualizando a imagem do fundo
            self.background_y += self.background_scroll_speed
            self.screen.blit(self.background, (0, self.background_y))
            self.screen.blit(self.background, (0, self.background_y - self.screen_height))

            if self.background_y >= self.screen_height:
                self.background_y = 0

            # Movimento da sprite do jogador
            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.player.blit(self.screen)

            # print(f'{self.player.is_jumping=}')

            #pontuacao
            self.score.regularScore()
            font = pygame.font.SysFont('sans',40)
            score_text = f'SCORE: {int(self.score.score)}'
            scoreShow = font.render(score_text, True, (255, 0, 251))
            self.screen.blit(scoreShow, (10, 10))

            


            pygame.display.flip()
            self.clock.tick(60)