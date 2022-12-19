#音乐播放器类

import pygame

class Music_Player():

    def __init__(self,path):
        self.path = path
        print('正在播放音乐')
        music = pygame.mixer.music.load(path)

    def play(self):
        print('正在播放音乐')
        # 检查是否正在播放音乐
        #if pygame.mixer.music.get_busy() == False:
            # 开始播放音乐流
        pygame.mixer.music.play()