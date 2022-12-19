#棋子类
import pygame
import contorller
from src import color


class ChessPieces():
    #type~棋子的类型
    #type ----  1   黑棋
    #type ----  0   白棋

    #检查当前位置是否已经落子
    def check_over_pos(self,pos_x, pos_y, over_pos):
        for val in contorller.control.over_pos:
            if val[0][0] == pos_x and val[0][1] == pos_y:
                return False
        return True

    # 落子
    def addChessPieces(self,pos_x,pos_y,bg,type):
        contorller.control.over_pos[(pos_x,pos_y)] = type
        pygame.draw.circle(bg, color.Color.BLACK, (pos_x, pos_y), 6, 6)

    # 判断是否获胜
    #def win(self):