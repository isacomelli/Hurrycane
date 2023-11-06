import pygame
import Constants

class Player:
    def __init__(self, game, x, y, player_name):
        self.game = game
        self.running_images = [pygame.image.load(f'img\\{player_name}_running_{x}.png') for x in range(1, 13)]
        self.running_images += self.running_images[-2::-1][:-1]
        self.current_image_number = 0
        self.image = self.running_images[self.current_image_number]
        self.image = pygame.transform.scale(self.image, (70, 106))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 8  # cada personagem vai ter uma velocidade e altura do pulo; dá pra fazer um a if nome x else b em cada
        self.jump_height = 12
        self.is_jumping = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.image = self.running_images[self.current_image_number]
        if not self.is_jumping:
            self.current_image_number = (self.current_image_number + 1) % len(self.running_images)
        self.rect.x = max(Constants.PLAYER_LANE_MIN_X - 8, min(self.rect.x, Constants.PLAYER_LANE_MAX_X + 8))

        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
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