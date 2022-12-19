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
        # 检查是否正在播放音乐
        if not pygame.mixer.music.get_busy():
            # 开始播放音乐流
            pygame.mixer.music.play(loops=self.type)

    def stop(self):
        pygame.mixer.music.stop()