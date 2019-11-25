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


clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    text_obj_render, text_rect = environment_msg_text('ProterozoicEra')
    environment()
    screen.blit(environment.image, environment.rect)
    screen.blit(text_obj_render, text_rect)

    pygame.display.flip()

pygame.quit()


