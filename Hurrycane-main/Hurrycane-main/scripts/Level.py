import pygame
import sys
import Constants, Item

class Level:
    def __init__(self, game, sceneManager):
        self.game = game
        self.sceneManager = sceneManager
        pygame.display.set_caption(Constants.GAME_NAME)
        self.player = game.player
        self.time = 0
        self.item_teste = 0
        self.background_y = 0
        self.createItem = True
        self.item = None
        self.item_json = None
        self.level_speed = None

    def run(self):
        pass

    def default_setups(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualizando a imagem do fundo
        self.background_y += self.level_speed
        self.game.screen.blit(self.background, (0, self.background_y))
        self.game.screen.blit(self.background, (0, self.background_y - Constants.SCREEN_HEIGHT))

        if self.background_y >= Constants.SCREEN_HEIGHT:
            self.background_y = 0

        # Movimento da sprite do jogador
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        self.player.blit(self.game.screen)

        # Movimento da sprite dos itens
        if self.createItem:
            if self.item_teste % 2 == 0:
                self.item = Item.Item(self.item_json[1])
            else:
                self.item = Item.Item(self.item_json[2])
            self.createItem = False
            self.item_teste += 1

        self.item.move()
        self.item.blit(self.game.screen)

        if self.player.rect.colliderect(self.item.rect):
            # colocar música
            self.game.score.update_score(self.item.score)
            self.createItem = True

        if self.item.rect.y >= Constants.SCREEN_HEIGHT:
            self.createItem = True

        #pontuacao
        self.game.score.regular_score()
        score_render = self.game.score.get_score_render()
        self.game.screen.blit(score_render, (10, 10))

        pygame.display.update()
        self.time += self.game.clock.tick(Constants.FPS)
        print(self.time) 
        # self.game.clock.tick(Constants.FPS)