#信息域类
import pygame
import color

class MsgView():

    def show(self):
        # 设置信息域大小
        x_size = 403
        y_size = 797
        msgview = pygame.Surface((x_size, y_size), flags=pygame.HWSURFACE)

        bg_color = color.Color.BROWN
        # 设置背景颜色
        msgview.fill(bg_color)

        return msgview