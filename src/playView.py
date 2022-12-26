#游戏界面
import sys
import pygame
import musicPlayer


class PlayView():
    def show(self):

        player_bg = musicPlayer.Music_Player('../mp3/test.mp3', -1)
        player_bg.volume(0.1)

        player_bg.play()

        def black(x, y):
            a = 20
            b = 20
            c = 20
            d = 0
            for i in range(50):
                pygame.draw.circle(screen, (a, b, c), [19.5 + 32 * x, 19.5 + 32 * y], (10 / (d - 5) + 10) * 1.6)
                a += 1
                b += 1
                c += 1
                d += 0.08
            pygame.display.update()

        def white(x, y):
            a = 170
            b = 170
            c = 170
            d = 0
            for i in range(50):
                pygame.draw.circle(screen, (a, b, c), [19.5 + 32 * x, 19.5 + 32 * y], (10 / (d - 5) + 10) * 1.6)
                a += 1
                b += 1
                c += 1
                d += 0.08
            pygame.display.update()

        screen = pygame.display.set_mode((615, 615))

        def end():
            pygame.font.init()
            text = font1.render("{}赢了".format(wb1), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (307.5, 307.5)
            screen.blit(text, textRect)
            pygame.display.flip()
            player_bg.stop()
            print(wb1)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player = musicPlayer.Music_Player('../mp3/index_bm.mp3', -1)
                        player.volume(1)
                        player.play()
                        return False


        pygame.display.set_caption('博弈中')
        screen.fill("#DD954F")
        a = pygame.Surface((603, 603), flags=pygame.HWSURFACE)
        a.fill(color='#121010')
        b = pygame.Surface((585, 585), flags=pygame.HWSURFACE)
        b.fill(color="#DD954F")
        c = pygame.Surface((579, 579), flags=pygame.HWSURFACE)
        c.fill(color='#121010')
        d = pygame.Surface((576, 576), flags=pygame.HWSURFACE)
        d.fill(color="#DD954F")
        e = pygame.Surface((31, 31), flags=pygame.HWSURFACE)
        e.fill(color="#DD954F")
        screen.blit(a, (6.5, 6.5))
        screen.blit(b, (15, 15))
        screen.blit(c, (18, 18))
        for j in range(18):
            for i in range(18):
                screen.blit(e, (20 + 32 * i, 20 + 32 * j))
        alist = []
        for j in range(19):
            alistone = []
            for i in range(19):
                alistone.append(0)
            alist.append(alistone)
        pygame.draw.circle(screen, '#121010', [307.5, 307.5], 5)
        pygame.draw.circle(screen, '#121010', [115.5, 307.5], 5)
        pygame.draw.circle(screen, '#121010', [499.5, 307.5], 5)
        pygame.draw.circle(screen, '#121010', [115.5, 499.5], 5)
        pygame.draw.circle(screen, '#121010', [499.5, 499.5], 5)
        pygame.draw.circle(screen, '#121010', [115.5, 115.5], 5)
        pygame.draw.circle(screen, '#121010', [499.5, 115.5], 5)
        pygame.draw.circle(screen, '#121010', [307.5, 499.5], 5)
        pygame.draw.circle(screen, '#121010', [307.5, 115.5], 5)
        pygame.display.flip()
        wb = "black"
        font1 = pygame.font.Font('../font/font.ttf', 120)

        keep = True

        while keep:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = round((x - 19.5) / 32)
                    y = round((y - 19.5) / 32)
                    if x < 0:
                        x = 0
                    if x > 18:
                        x = 18
                    if y < 0:
                        y = 0
                    if y > 18:
                        y = 18

                    if alist[x][y] == 0:
                        eval(wb + "({},{})".format(x, y))
                        if wb == "black":
                            alist[x][y] = 1
                            wb1 = "小黑子"
                            wb = "white"
                        elif wb == "white":
                            alist[x][y] = 2
                            wb1 = "白棋"
                            wb = "black"
                        xx = x
                        yy = y
                        while True:
                            if xx == 0:
                                break
                            elif alist[xx][yy] != alist[x][y]:
                                xx += 1
                                break
                            else:
                                xx -= 1
                        num = 0
                        while True:
                            if xx == 18:
                                break
                            elif alist[xx][yy] != alist[x][y]:
                                break
                            else:
                                xx += 1
                                num += 1
                        if num >= 5:
                            keep = end()


                        xx = x
                        yy = y
                        while True:
                            if yy == 0:
                                break
                            elif alist[xx][yy] != alist[x][y]:
                                yy += 1
                                break
                            else:
                                yy -= 1
                        num = 0
                        while True:
                            if yy == 18:
                                break
                            elif alist[xx][yy] != alist[x][y]:
                                break
                            else:
                                yy += 1
                                num += 1
                        if num >= 5:
                            keep = end()


                        xx = x
                        yy = y
                        while True:
                            if xx == 0:
                                break
                            elif yy == 0:
                                break
                            elif alist[xx][yy] != alist[x][y]:
                                xx += 1
                                yy += 1
                                break
                            else:
                                xx -= 1
                                yy -= 1
                        num = 0
                        while True:
                            if xx == 18:
                                break
                            elif yy == 18:
                                break
                            elif alist[xx][yy] != alist[x][y]:
                                break
                            else:
                                xx += 1
                                yy += 1
                                num += 1
                        if num >= 5:
                            keep = end()


                        xx = x
                        yy = y
                        while True:
                            if xx == 0:
                                break
                            elif yy == 18:
                                break
                            elif alist[xx][yy] != alist[x][y]:
                                xx += 1
                                yy -= 1
                                break
                            else:
                                xx -= 1
                                yy += 1
                        num = 0
                        while True:
                            if xx == 18:
                                break
                            elif yy == 0:
                                break
                            elif alist[xx][yy] != alist[x][y]:
                                break
                            else:
                                xx += 1
                                yy -= 1
                                num += 1
                        if num >= 5:
                            keep = end()