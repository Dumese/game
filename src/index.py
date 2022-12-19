# 主页类
import sys
import pygame
import musicPlayer
import playView
import color
import rulesView


class Index():

    def show(self):

        # 初始化pygame
        pygame.init()

        player = musicPlayer.Music_Player('../mp3\index_bm.mp3', -1)
        player.play()

        play = playView.PlayView()

        rule = rulesView.RulesView()

        font = pygame.font.Font('../font/font.ttf', 50)
        text = font.render("规则说明", True, color.Color.RED, color.Color.WOOD)

        '''
        # 获得显示对象的 rect区域大小
        textRect = text.get_rect()
        print(textRect)
        '''

        while True:

            # 设置标题
            pygame.display.set_caption("混元形意五子棋")

            # 设置显示窗口的大小
            screen_width = 620
            screen_height = 840
            screen = pygame.display.set_mode((screen_width, screen_height))

            # 设置背景图片
            bg_img = pygame.image.load("../img/index_bg.png")
            play_img = pygame.image.load("../img/play.png")

            screen.blit(bg_img, (0, 0))
            screen.blit(play_img, (160, 525))

            screen.blit(text, (20, 20))

            # 获取循环事件，监听事件
            for event in pygame.event.get():
                # 判断用户是否点击了关闭按钮
                if event.type == pygame.QUIT:
                    # 卸载所有的模块
                    pygame.quit()
                    sys.exit()

                # 判断用户是否点击了开始按钮
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x > 160 and mouse_x < 360 and mouse_y < 600 and mouse_y > 525:
                        player.stop()
                        play.show()

                #判断用户是否点击了规则按钮
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x > 20 and mouse_x < 220 and mouse_y < 90 and mouse_y > 20:
                        rule.show()

            pygame.display.flip()
