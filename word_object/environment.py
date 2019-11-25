from setting import *
import pygame


class Environment(object):
    def __init__(self):
        self.image = pygame.image.load('./images/sea.png')
        self.rect = self.image.get_rect()
        self.image_width, self.image_height = self.rect[2:]
        self.position_x = (WIDTH - self.image_width) / 2
        self.position_y = (HEIGHT - self.image_height) / 2
        self.speed = 5

    def __call__(self):
        pass

    def draw_bg(self, screen):
        self.rect.left += 1
        screen.blit(self.image, self.rect)
