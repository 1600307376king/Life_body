from setting import *
from word_object.text import Text
from word_object.environment import Environment
import sys
import pygame


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('ProterozoicEra')
environment = Environment()
environment_msg_text = Text()

time_frame = 0
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    environment.draw_bg(screen)
    environment_msg_text.draw(screen, 'ProterozoicEra')
    time_frame += 1
    pygame.display.flip()

pygame.quit()


