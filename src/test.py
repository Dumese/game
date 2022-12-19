import pygame

print(pygame.font.get_fonts())
import sys
import pygame

# 初始化
pygame.init()
screen = pygame.display.set_mode((600,400))
#填充主窗口的背景颜色
screen.fill((20,90,50))
#设置窗口标题
pygame.display.set_caption('c语言中文网')


f = pygame.font.Font('../font/font.ttf',50)

# render(text, antialias, color, background=None) -> Surface
text = f.render("网址：c.biancheng.net",True,(255,0,0),(255,255,255))

#获得显示对象的 rect区域大小
textRect =text.get_rect()

#设置显示对象居中
textRect.center = (300,200)
screen.blit(text,textRect)

while True:
    # 循环获取事件，监听事件
    for event in pygame.event.get():
        # 判断用户是否点了关闭按钮
        if event.type == pygame.QUIT:
            #卸载所有pygame模块
            pygame.quit()
            #终止程序
            sys.exit()
    pygame.display.flip() #更新屏幕内容