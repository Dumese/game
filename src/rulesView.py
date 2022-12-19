#规则类
import sys

import pygame

class RulesView():

    bg_img = pygame.image.load("../img/rules_bg.png")

    def show(self):

        keep = True

        while keep:
            pygame.display.set_caption("规则")
            screen_width = 620
            screen_height = 840
            screen = pygame.display.set_mode((screen_width, screen_height))
            screen.blit(self.bg_img, (0, 0))
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
                    if mouse_x > 0 and mouse_x < 220 and mouse_y < 90 and mouse_y > 0:
                        keep = False
            pygame.display.flip()