#音乐播放器类

import pygame

class Music_Player():



    def __init__(self,path,type):
        self.path = path
        self.type = type
        print('正在初始化音乐播放器')
        pygame.mixer.music.load(path)


    def play(self):
        print('正在播放音乐')
        pygame.mixer.init()
        # 开始播放音乐流
        pygame.mixer.music.play(loops=self.type)

    #设置音量
    def volume(self,num):
        pygame.mixer.music.set_volume(num)

    def stop(self):
        pygame.mixer.music.stop()