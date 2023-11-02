# ISA comentários
# - pensei em cada personagem ter uma velocidade e altura do pulo, não os dois ser fixo
# - essa seria a classe mãe, não sei se as filhas (Ariel e o outro personagem) seria legal de colocar em outro arquivo ou manter aqui

import pygame

class Player:
    def __init__(self, game, x, y, image_path):
        self.game = game
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3
        self.jump_height = 12
        self.is_jumping = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.rect.x = max(0, min(self.game.screen_width - self.rect.width, self.rect.x))

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