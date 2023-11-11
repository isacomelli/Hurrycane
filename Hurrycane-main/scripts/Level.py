import pygame, sys, random
import Constants, Item

class Level:
    def __init__(self, game, sceneManager):
        self.game = game
        self.sceneManager = sceneManager
        pygame.display.set_caption(Constants.GAME_NAME)
        self.player = game.player
        self.clock = pygame.time.Clock()
        self.time = 0
        self.background_y = 0
        self.rain = pygame.image.load(f'img\\rain.png')
        self.rain = pygame.transform.scale(self.rain, (Constants.SCREEN_WIDTH * 2, Constants.SCREEN_HEIGHT * 2))
        self.rain_x = -100
        self.rain_y = 0
        self.create_item = True
        self.item = None
        self.item_json = None
        self.level_speed = None
        self.good_item_sound = pygame.mixer.Sound(Constants.MENU_SELECT_SOUND)
        self.bad_item_sound = pygame.mixer.Sound(Constants.BAD_ITEM_SOUND)

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

        # Movimento da sprite dos itens
        if self.create_item:
            self.item = Item.Item(self.item_json[random.choice(list(self.item_json.keys()))])
            self.create_item = False

        self.item.move()
        self.item.blit(self.game.screen)

        # Movimento da sprite do jogador
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        self.player.blit(self.game.screen)

        player_foot = (self.player.rect.x, self.player.rect.y + self.player.rect.height - 10)
        player_foot_rect = pygame.Rect(player_foot, (self.player.rect.width, 10))

        if player_foot_rect.colliderect(self.item.rect) and not self.player.is_jumping:
            self.game.score.update_score(self.item.score)
            if self.item.type == 'good':
                self.good_item_sound.play()
            else:
                self.bad_item_sound.play() 
            self.create_item = True

        if self.item.rect.y >= Constants.SCREEN_HEIGHT:
            self.create_item = True
            
        self.game.hurrycane.move()
        self.game.hurrycane.blit(self.game.screen)

        if self.sceneManager.get_state() == 'streetTwo':
            self.rain_x += self.level_speed
            self.rain_y += self.level_speed * 1.25
            self.game.screen.blit(self.rain, (self.rain_x, self.rain_y))
            self.game.screen.blit(self.rain, (self.rain_x, self.rain_y - Constants.SCREEN_HEIGHT))

            if self.rain_y >= Constants.SCREEN_HEIGHT:
                self.rain_y = 0
            if self.rain_x >= Constants.SCREEN_WIDTH / 10:
                self.rain_x = -100

        #pontuacao
        self.game.score.regular_score()
        score_render, shadow_score_render = self.game.score.get_score_render()
        self.game.screen.blit(shadow_score_render, (7, 7))
        self.game.screen.blit(score_render, (10, 10))

        pygame.display.update()
        # self.time += self.game.clock.tick(Constants.FPS)
        self.time += self.clock.tick(Constants.FPS)
        # self.game.clock.tick(Constants.FPS)