import sys

import pygame
import soundPlayer
def do():
    pygame.init()

    sound1 = soundPlayer.Sound_Player('../mp3/whiteLose.mp3')

    sound1.play()

    while True:
        # 设置标题
        pygame.display.set_caption("混元形意五子棋")

        # 设置显示窗口的大小
        screen_width = 620
        screen_height = 840
        screen = pygame.display.set_mode((screen_width, screen_height))

        # 获取循环事件，监听事件
        for event in pygame.event.get():
            # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:
                # 卸载所有的模块
                pygame.quit()
                sys.exit()

            #if event.type == pygame.MOUSEBUTTONDOWN:


do()