import pygame, sys, random
import Constants, Item

class Level:
    def __init__(self, game):
        self.game = game
        self.sceneManager = game.sceneManager
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

    def update_player_lives_display(self):
        heart_image = pygame.image.load(f'img\\heart_{self.player.lives}.png')
        heart_image = pygame.transform.scale(heart_image, (100, 30))
        heart_rect = heart_image.get_rect()
        heart_rect.topright = (Constants.SCREEN_WIDTH - 10, 8)

        self.game.screen.blit(heart_image, heart_rect)

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

        # Atualizando a imagem dos itens
        self.run_IA()
        self.move_items()

        # Atualizando a imagem do jogador
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        self.player.blit(self.game.screen)
        
        # Atualizando a imagem do furacão
        self.game.hurrycane.move()
        self.game.hurrycane.blit(self.game.screen)

        # Atualizando a imagem da chuva
        if self.sceneManager.get_state() == 'streetTwo':
            self.rain_x += self.level_speed
            self.rain_y += self.level_speed * 1.25
            self.game.screen.blit(self.rain, (self.rain_x, self.rain_y))
            self.game.screen.blit(self.rain, (self.rain_x, self.rain_y - Constants.SCREEN_HEIGHT))

            if self.rain_y >= Constants.SCREEN_HEIGHT:
                self.rain_y = 0
            if self.rain_x >= Constants.SCREEN_WIDTH / 10:
                self.rain_x = -100

        # Pontuação
        self.game.score.regular_score()
        score_render, shadow_score_render = self.game.score.get_score_render()
        self.game.screen.blit(shadow_score_render, (7, 7))
        self.game.screen.blit(score_render, (10, 10))

        # Atualizando a imagem das vidas
        self.update_player_lives_display()

        pygame.display.update()
        self.time += self.clock.tick(Constants.FPS)
        # print(f'{self.player.good_streak=}')
        # print(f'{self.generate_min_range=}')
        # print(f'{self.player.lives=}')

    ##### IA
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
            random_item = random.choice(list(items_filtered.keys()))
            if 'hole' in random_item:
                self.item_list.insert(0, Item.Item(items_filtered[random_item],item_x))
            else:
                self.item_list.append(Item.Item(items_filtered[random_item],item_x))

    def move_items(self):
        player_collide = (self.player.rect.x, self.player.rect.y + self.player.rect.height - 40)
        player_collide_rect = pygame.Rect(player_collide, (self.player.rect.width, 40))

        for item in self.item_list:
            item.move()
            item.blit(self.game.screen)

        for item in self.item_list:
            if player_collide_rect.colliderect(item.rect) and not self.player.is_jumping:
                self.game.score.update_score(item.score * self.multiplier + self.player.good_streak)
                if item.type == 'good':
                    self.player.good_streak += 1
                    if self.game.sound_on:
                        self.good_item_sound.play()
                else:
                    self.player.lives -= 1
                    self.player.good_streak = 0
                    if self.game.sound_on:
                        self.bad_item_sound.play()

                self.item_list.remove(item)

            if item.rect.y >= Constants.SCREEN_HEIGHT:
                self.item_list.remove(item)