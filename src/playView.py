#游戏界面
import sys

import pygame
import chessBorad
import msgView
import color

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

            #获取鼠标坐标信息
            pos_x, pos_y = pygame.mouse.get_pos()

            '''
            # 找到显示的可以落子的位置
            def find_pos(pos_x, pos_y):
                for i in range(27, 670, 44):
                    for j in range(27, 670, 44):
                        L1 = i - 22
                        L2 = i + 22
                        R1 = j - 22
                        R2 = j + 22
                        if pos_x >= L1 and pos_x <= L2 and pos_y >= R1 and pos_y <= R2:
                            return i, j
                return pos_x, pos_y

            pos_x, pos_y = find_pos(pos_x, pos_y)
            pygame.draw.rect(screen, [0, 229, 238], [pos_x - 22, pos_y - 22, 28, 28], 2, 1)
            '''
            def find_pos(pos_x, pos_y):
                for i in range(28, 808, 39):
                    for j in range(28, 808, 39):
                        L1 = i - 19
                        L2 = i + 19
                        R1 = j - 19
                        R2 = j + 19
                        if pos_x >= L1 and pos_x <= L2 and pos_y >= R1 and pos_y <= R2:
                            return i, j
                return pos_x, pos_y

            set_x, set_y = find_pos(pos_x, pos_y)
            print(set_x,set_y)

            if pos_x >= 9 and pos_x <= 788 and pos_y >= 9 and pos_y <= 788:
                pygame.draw.rect(screen, color.Color.WHITE, [set_x - 19, set_y - 19, 38, 38], 2, 1)
                #获取鼠标按下左键
                keys_pressed = pygame.mouse.get_pressed()
                if keys_pressed[0] == True:
                    print('鼠标按下左键')
                    print(set_x, set_y)


            pygame.display.flip()