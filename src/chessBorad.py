import pygame
import color

#棋盘类
class Chessborad():

    def show(self):
        #设置棋盘大小
        size = 797
        borad = pygame.Surface((size,size),flags=pygame.HWSURFACE)

        bg_color= color.Color.BROWN

        #设置线条颜色
        line_color = color.Color.BLACK
        #设置背景颜色
        borad.fill(bg_color)

        #绘制边框
        for pos in range(28,size + 11,39):
            #绘制竖线
            #边框线加粗
            if pos == 28 or pos == size - 28:
                pygame.draw.line(borad,line_color,[pos,28],[pos,size-28],4)
            else:
                pygame.draw.line(borad,line_color,[pos,28],[pos,size-28],2)

            #绘制横线
            if pos == 28 or pos == size - 28:
                pygame.draw.line(borad,line_color,[28,pos],[size-28,pos],4)
            else:
                pygame.draw.line(borad,line_color,[28,pos],[size-28,pos],2)

        #绘制圆点
        for pos_x in (145,379,613):
            for pos_y in (145,379,613):
                pygame.draw.circle(borad, color.Color.BLACK, (pos_x, pos_y), 6, 6)
        return borad