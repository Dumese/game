import pygame
import color
#文本域类

class TextView():

    def __init__(self,text):
        self.text = text

    def show(self,bg_color = color.Color.WHITE,font_color = color.Color.BLACK,font_size = 50):
        font = pygame.font.Font('../font/font.ttf', font_size)
        textview = font.render(self.text, True, font_color, bg_color)
        # 获得显示对象的 rect区域大小
        textRect = textview.get_rect()
        print(textRect)
        return textview