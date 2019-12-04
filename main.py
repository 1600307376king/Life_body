from setting import *
from world_object.text import Text
from world_object.environment import Environment
from world_object.ball import Ball
import sys
import pygame
import time
import datetime


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('ProterozoicEra')
environment = Environment()
environment_msg_text = Text()
ball = Ball()
clock = pygame.time.Clock()

current_time = INITIAL_TIME

while True:
    clock.tick(FRAMES_NUMBER)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    current_time += 1
    environment.draw_bg(screen)
    environment_msg_text.draw(screen, 'ProterozoicEra')
    ball.display_speed_text(screen, environment_msg_text, current_time)
    ball.change_ball_state(screen, 1/FRAMES_NUMBER, environment)

    pygame.display.flip()


pygame.quit()


