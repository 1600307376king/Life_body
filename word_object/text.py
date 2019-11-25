import pygame


class Text(object):
    def __init__(self):
        self.type_face = 'constan.ttf'
        self.font_position = (20, 20)
        self.background_color = None
        self.color = (0, 0, 0)
        self.font_size = 24
        self.text = ''

    def draw(self, screen, text, color=None, font_size=None, position=None, background_color=None,
             type_face=None):
        self.type_face = type_face
        self.font_position = position
        self.background_color = background_color
        self.color = color
        self.font_size = font_size
        self.text = text

        text_obj = pygame.font.Font('./font/constan.ttf', 24)
        text_obj_render = text_obj.render(text, True, (0, 0, 0), self.background_color)
        text_rect = text_obj_render.get_rect()
        text_rect.center = (120, 20)
        screen.blit(text_obj_render, text_rect)
