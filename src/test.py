# -*-coding:GBK -*-
import pygame

file = 'mp3\index_bm.mp3'  # Ҫ���ŵĸ������ص�ַ
pygame.mixer.init()  # mixer�ĳ�ʼ��
print("��־�� - û�뿪��")  # �����ʾҪ���ŵĸ���
pygame.mixer.music.load(file)  # ����һ�������ļ����ڲ���

while True:
    # ������������ţ��з���True��û�з���False
    # ���û����������ѡ�񲥷�
    if not pygame.mixer.music.get_busy():  # ����Ƿ����ڲ�������
        pygame.mixer.music.play()  # ��ʼ����������