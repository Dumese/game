#游戏界面
import sys

import pygame
import chessBorad
import msgView

class PlayView():

    borad = chessBorad.Chessborad().show()
    msgview = msgView.MsgView.show(None)
    def show(self):
        while True:
            pygame.display.set_caption("混元形意五子棋")
            screen_width = 1200
            screen_height = 797
            screen = pygame.display.set_mode((screen_width, screen_height))
            screen.blit(self.borad, (0, 0))
            screen.blit(self.msgview,(797,0))

            # 获取循环事件，监听事件
            for event in pygame.event.get():
                # 判断用户是否点击了关闭按钮
                if event.type == pygame.QUIT:
                    # 卸载所有的模块
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()