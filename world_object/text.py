import pygame


class Text(object):
    def __init__(self):
        # 字体类型
        self.typeface = 'constan.ttf'
        self.font_position = (20, 20)
        self.background_color = None
        self.color = (0, 0, 0)
        self.font_size = 24
        self.text = ''
        # 文字显示频率
        self.frequency = 10

    # 绘制文字 / draw text
    def draw(self, screen, text, color=(0, 0, 0), font_size=24, position=(20, 20), background_color=None,
             typeface='constan.ttf'):
        self.typeface = typeface
        self.font_position = position
        self.background_color = background_color
        self.color = color
        self.font_size = font_size
        self.text = text

        text_obj = pygame.font.Font('./font/' + str(self.typeface), self.font_size)
        text_obj_render = text_obj.render(text, True, self.color, self.background_color)
        text_rect = text_obj_render.get_rect()
        text_rect.center = self.font_position
        screen.blit(text_obj_render, text_rect)
