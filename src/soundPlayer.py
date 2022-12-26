#音效播放类

import pygame

class Sound_Player():
    def __init__(self,path):
        pygame.mixer.Sound(path)

    def play(self):
        pygame.mixer.Sound.play(loops=1)