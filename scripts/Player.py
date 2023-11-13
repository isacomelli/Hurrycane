import pygame
import Constants

class Player:
    def __init__(self, game, player_name):
        self.game = game
        self.images = [pygame.image.load(f'img\\{player_name}_{x}.png') for x in range(1, 13)]
        self.images += self.images[-2::-1][:-1]
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image, (70, 106))
        self.rect = self.image.get_rect()
        self.rect.center = (Constants.SCREEN_WIDTH // 2, Constants.SCREEN_HEIGHT - 150)
        self.speed = (8 if player_name == 'ariel' else 4)
        self.jump_height = (10 if player_name == 'ariel' else 7) 
        self.jump_sound = pygame.mixer.Sound(Constants.JUMP_SOUND)
        self.is_jumping = False
        self.jump_sound.set_volume(0.10)
        self.good_streak = 0

    def move(self, keys): 
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.image = self.images[self.current_image]
        if not self.is_jumping:
            self.current_image = (self.current_image + 1) % len(self.images)
        self.rect.x = max(Constants.PLAYER_LANE_MIN_X - 8, min(self.rect.x, Constants.PLAYER_LANE_MAX_X + 8))

        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.jump_sound.play()
                self.is_jumping = True
                self.jump_pixels = self.jump_height

        if self.is_jumping:
            if self.jump_pixels >= -self.jump_height:
                self.rect.y -= self.jump_pixels
                self.jump_pixels -= 1
            else:
                self.is_jumping = False

    def blit(self, surface):
        surface.blit(self.image, self.rect.topleft)