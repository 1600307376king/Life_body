#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 0004 13:57
# @Author  : HelloWorld
# @File    : ball.py
import pygame
import math
from setting import *
from world_object.text import Text

# 小球初始速度 / the initial speed of the ball
init_ball_speed = 0.0
# 小球初始位置 / the initial position of the ball
init_x, init_y = (300.0, 100.0)


class Ball(object):

    def __init__(self):
        # unit: kg
        self.mass = 1000.0
        # unit: meters
        self.radius = 10.0
        self.color = (205, 149, 12)
        self.cur_x = init_x
        self.cur_y = init_y
        self.direction = [0, 1, 2, 3, 4]
        self.speed = init_ball_speed

    # 画出小球 / draw a ball
    def show(self, screen):
        return pygame.draw.circle(screen, self.color, (math.floor(self.cur_x), math.floor(self.cur_y)),
                                  math.floor(self.radius), 0)

    # 小球运动 / changing the state of ball
    def change_ball_state(self, screen, time_frame, env):
        current_g = env.get_gravitation(env.mass, self.mass, self.radius + env.radius + HEIGHT - self.cur_y)
        ball_acceleration = env.get_nt_second_law(current_g, self.mass)

        self.speed += ball_acceleration * time_frame
        if self.cur_y > 700:
            self.speed = 0.0
        self.cur_y += self.speed * time_frame * self.direction[1]
        self.show(screen)

    # 获得小球速度 / get current ball speed
    def get_cur_speed(self):
        return round(self.speed, 2)

    # 小球显示速度 / display ball speed value
    def display_speed_text(self, screen, env_text, cur_time_frame):
        global init_ball_speed
        if cur_time_frame % env_text.frequency == 0:
            init_ball_speed = self.get_cur_speed()
        env_text.draw(screen, str(init_ball_speed),
                      color=(255, 106, 106), font_size=16, position=(80, 80), typeface='georgia.ttf')

    # 小球对其他物体的作用力 / the force of the ball on other objects
    def ball_to_other_force(self, a, time_difference, other_speed=0):
        relative_speed = self.speed - other_speed
        force = self.mass * a + self.mass * relative_speed / time_difference
        return force

