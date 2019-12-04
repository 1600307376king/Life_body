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
        # unit: N·m²/kg²
        self.G = 6.67e-11
        # unit: kg
        self.mass = 5.965e24
        # unit: meter
        self.radius = 6371e3

    def __call__(self):
        pass

    # 绘制游戏背景 / draw the game's background
    def draw_bg(self, screen):
        # self.rect.left += 1
        screen.blit(self.image, self.rect)

    # 获取当前引力 / get current gravitation
    def get_gravitation(self, m1, m2, r):
        f = self.G * m1 * m2 / (r**2)
        return f

    # 获取加速度 /get the current acceleration
    @staticmethod
    def get_acceleration(dx, dt):
        a = dx / (dt ** 2)
        return a

    # 牛顿第二定律计算加速度 / use Newton's second law to calculate acceleration
    @staticmethod
    def get_nt_second_law(f, m):
        a = f / m
        return a
