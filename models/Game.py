# ISA - Comentários
# - Aqui o personagem tá fixo, mas depois de criar o menu, vai se tornar variável
# - prof passou nada de POO em python, mas:
#   - Constantes não precisam ir dentro de __init__, podem ir fora sem usar o self; acho aplicável para o tamanho da tela, mas tbm não é um problema ir ali
#   - Todos os atributos e métodos estão em public... não sei se seria um problema manter, mas acho q não

import pygame
import sys
from models import Player

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
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

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

            pygame.display.flip()
            self.clock.tick(60)