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
        self.level_speed = None
        self.good_item_sound = pygame.mixer.Sound(Constants.MENU_SELECT_SOUND)
        self.bad_item_sound = pygame.mixer.Sound(Constants.BAD_ITEM_SOUND)

        # IA attributes
        self.item_list = []
        self.generate_min_range = 40
        self.good_item_generate_chance = 50
        self.player_lane_generate_chance = 50

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
        # if self.create_item:
        #     self.item = Item.Item(self.items[random.choice(list(self.items.keys()))])
        #     self.create_item = False

        # self.item.move()
        # self.item.blit(self.game.screen)

        self.run_IA()
        self.move_items()

        # Movimento da sprite do jogador
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        self.player.blit(self.game.screen)

        # player_collide = (self.player.rect.x, self.player.rect.y + self.player.rect.height - 10)
        # player_collide_rect = pygame.Rect(player_collide, (self.player.rect.width, 10))

        # if player_collide_rect.colliderect(self.item.rect) and not self.player.is_jumping:
        #     self.game.score.update_score(self.item.score)
        #     if self.item.type == 'good':
        #         self.good_item_sound.play()
        #     else:
        #         self.bad_item_sound.play() 
        #     self.create_item = True

        # if self.item.rect.y >= Constants.SCREEN_HEIGHT:
        #     self.create_item = True
            
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
        self.time += self.clock.tick(Constants.FPS)
        # print(f'{self.player.good_streak=}')
        # print(f'{self.generate_min_range=}')

    ##### IA #####
    def run_IA(self):
        if self.player.good_streak >= 9:
            self.generate_min_range = 15
            self.good_item_generate_chance = 20
            self.player_lane_generate_chance = 65
        elif self.player.good_streak >= 6:
            self.generate_min_range = 20
            self.good_item_generate_chance = 30
            self.player_lane_generate_chance = 60
        elif self.player.good_streak >= 3:
            self.generate_min_range = 25
            self.good_item_generate_chance = 40
            self.player_lane_generate_chance = 55
        else:
            self.generate_min_range = 30
            self.good_item_generate_chance = 50
            self.player_lane_generate_chance = 50
    
        if self.time % random.randint(self.generate_min_range, 100) == 0 or len(self.item_list) < 2:
            if random.randint(1, 100) > self.good_item_generate_chance:
                generate_item_type = 'bad'
            else:
                generate_item_type = 'good'

            if random.randint(1, 100) > self.player_lane_generate_chance:
                item_x = 0
            else:
                item_x = self.player.rect.x

            items_filtered = {id: item for id, item in self.items.items() if item['type'] == generate_item_type}
            self.item_list.append(Item.Item(items_filtered[random.choice(list(items_filtered.keys()))], item_x))

    def move_items(self):
        for index, item in enumerate(self.item_list):
            item.move()
            item.blit(self.game.screen)

            player_collide = (self.player.rect.x, self.player.rect.y + self.player.rect.height - 50)
            player_collide_rect = pygame.Rect(player_collide, (self.player.rect.width, 50))

            if player_collide_rect.colliderect(item.rect) and not self.player.is_jumping:
                self.game.score.update_score(item.score)
                if item.type == 'good':
                    self.player.good_streak += 1
                    self.good_item_sound.play()
                else:
                    self.player.good_streak = 0
                    self.bad_item_sound.play()
                self.item_list.pop(index)

            if item.rect.y >= Constants.SCREEN_HEIGHT:
                self.item_list.pop(index)