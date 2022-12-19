# 主页类
import sys
import pygame
import musicPlayer
import playView


class Index():

    def show(self):

        # 初始化pygame
        pygame.init()

        player = musicPlayer.Music_Player('mp3\index_bm.mp3',-1)
        player.play()

        play = playView.PlayView()


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

            # 获取循环事件，监听事件
            for event in pygame.event.get():
                # 判断用户是否点击了关闭按钮
                if event.type == pygame.QUIT:
                    # 卸载所有的模块
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x > 160 and mouse_x < 360 and mouse_y < 600 and mouse_y > 525:
                        player.stop()
                        play.show()


            pygame.display.flip()
