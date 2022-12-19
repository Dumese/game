#规则类
import sys
import pygame

import textView
import color

class RulesView():

    bg_img = pygame.image.load("../img/rules_bg.png")
    back = textView.TextView('返回')

    def show(self):

        keep = True

        while keep:
            pygame.display.set_caption("规则")
            screen_width = 620
            screen_height = 840
            screen = pygame.display.set_mode((screen_width, screen_height))
            screen.blit(self.bg_img, (0, 0))
            screen.blit(self.back.show(bg_color=color.Color.WOOD,font_color=color.Color.RED),(20,20))

            # 获取循环事件，监听事件
            for event in pygame.event.get():
                # 判断用户是否点击了关闭按钮
                if event.type == pygame.QUIT:
                    # 卸载所有的模块
                    pygame.quit()
                    sys.exit()

                # 判断用户是否点击了规则按钮
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x > 20 and mouse_x < 120 and mouse_y < 90 and mouse_y > 20:
                        keep = False
            pygame.display.flip()