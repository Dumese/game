# -*-coding:GBK -*-
import pygame

file = 'mp3\index_bm.mp3'  # 要播放的歌曲本地地址
pygame.mixer.init()  # mixer的初始化
print("林志炫 - 没离开过")  # 输出提示要播放的歌曲
pygame.mixer.music.load(file)  # 载入一个音乐文件用于播放

while True:
    # 检查音乐流播放，有返回True，没有返回False
    # 如果没有音乐流则选择播放
    if not pygame.mixer.music.get_busy():  # 检查是否正在播放音乐
        pygame.mixer.music.play()  # 开始播放音乐流