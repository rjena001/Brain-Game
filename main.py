import pygame as pg
import random, time, os
pg.init()
clicked = []
successful = []
tile_size = 0
complete = "menu"
r = 1
startGame = int(time.time())
if "highScore.txt" not in os.listdir("."):
    f = open("highScore.txt", "w")
    f.write(f"0\n0\n0\n0\n0")
    f.close()
def setGame(r):
    global successful, clicked, arr, tile_size, complete, startGame
    r*=2
    fakeArr = [0,1,2,3,4,5,6,7,8,9]
    for i in range(5):
        random.shuffle(fakeArr)
    arr = [[fakeArr[j] for j in range(r)] for i in range(r)]
    for i in arr:
        random.shuffle(i)
    random.shuffle(arr)
    clicked = []
    successful = []
    tile_size = width//r
    complete = "playing"
    startGame = int(time.time())
    return arr
running = True
width = 500
height = 500
screen = pg.display.set_mode((width, height))
font = pg.font.Font("freesansbold.ttf", 32)
paired = pg.mixer.Sound(".\\assets\\paired.wav")
success_sound = pg.mixer.Sound(".\\assets\\success.mp3")
c = 0
black = False
tf = False
def drawGrid():
    for i in range(int(width/tile_size)):
        if not black:
            pg.draw.rect(screen, (255,255,255), (0,tile_size*i, width, 2))
            pg.draw.rect(screen, (255,255,255), (tile_size*i, 0, 2, height))
        else:
            pg.draw.rect(screen, (0,0,0), (0,tile_size*i, width, 2))
            pg.draw.rect(screen, (0,0,0), (tile_size*i, 0, 2, height))
def change():
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if [i, j] in clicked or tf:
                if arr[i][j] == 0:
                    p1 = pg.image.load(".\\assets\\1.png")
                    p1 = pg.transform.scale(p1, (tile_size,tile_size))
                    screen.blit(p1, (tile_size*i, tile_size*j))
                if arr[i][j] == 1:
                    p2 = pg.image.load(".\\assets\\2.png")
                    p2 = pg.transform.scale(p2, (tile_size,tile_size))
                    screen.blit(p2, (tile_size*i, tile_size*j))
                if arr[i][j] == 2:
                    p3 = pg.image.load(".\\assets\\3.png")
                    p3 = pg.transform.scale(p3, (tile_size,tile_size))
                    screen.blit(p3, (tile_size*i, tile_size*j))
                if arr[i][j] == 3:
                    p4 = pg.image.load(".\\assets\\4.png")
                    p4 = pg.transform.scale(p4, (tile_size,tile_size))
                    screen.blit(p4, (tile_size*i, tile_size*j))
                if arr[i][j] == 4:
                    p5 = pg.image.load(".\\assets\\5.png")
                    p5 = pg.transform.scale(p5, (tile_size,tile_size))
                    screen.blit(p5, (tile_size*i, tile_size*j))
                if arr[i][j] == 5:
                    p6 = pg.image.load(".\\assets\\6.png")
                    p6 = pg.transform.scale(p6, (tile_size,tile_size))
                    screen.blit(p6, (tile_size*i, tile_size*j))
                if arr[i][j] == 6:
                    p7 = pg.image.load(".\\assets\\7.png")
                    p7 = pg.transform.scale(p7, (tile_size,tile_size))
                    screen.blit(p7, (tile_size*i, tile_size*j))
                if arr[i][j] == 7:
                    p8 = pg.image.load(".\\assets\\8.png")
                    p8 = pg.transform.scale(p8, (tile_size,tile_size))
                    screen.blit(p8, (tile_size*i, tile_size*j))
                if arr[i][j] == 8:
                    p9 = pg.image.load(".\\assets\\9.png")
                    p9 = pg.transform.scale(p9, (tile_size,tile_size))
                    screen.blit(p9, (tile_size*i, tile_size*j))
                if arr[i][j] == 9:
                    p10 = pg.image.load(".\\assets\\10.png")
                    p10 = pg.transform.scale(p10, (tile_size,tile_size))
                    screen.blit(p10, (tile_size*i, tile_size*j))
            else:
                pg.draw.rect(screen, (0,0,0), (tile_size*i, tile_size*j, tile_size, tile_size))
            if [i, j] in successful:
                pg.draw.rect(screen, (0,0,0), (tile_size*i, tile_size*j, tile_size, tile_size))
                success = pg.image.load(".\\assets\\success.gif")
                success = pg.transform.scale(success, (tile_size,tile_size))
                screen.blit(success, (tile_size*i, tile_size*j+5))

while running:
    for evt in pg.event.get():
        if evt.type == pg.QUIT or (evt.type == pg.KEYDOWN and evt.key == pg.K_q):
            running = False
            pg.quit()
        if complete == "playing":
            if evt.type == pg.KEYDOWN:
                if evt.key == pg.K_s:
                    tf = True
                    black = True
                if evt.key == pg.K_h:
                    tf = False
                    black = False
            if evt.type == pg.MOUSEBUTTONDOWN:
                x,y = evt.pos
                x, y = int(x/tile_size), int(y/tile_size)
                if [x,y] not in [*clicked, *successful]:
                    clicked.append([x,y])
                if len(clicked) == 2:
                    if clicked[0]!=clicked[1] and arr[clicked[0][0]][clicked[0][1]] == arr[clicked[1][0]][clicked[1][1]]:
                        successful.append(clicked[0])
                        successful.append(clicked[1])
                        paired.play()
                        clicked.clear()
                elif len(clicked)>2:
                    clicked = []
            if len(successful) == len(arr)*len(arr):
                complete = "success"
                success_sound.play()
        if complete == "menu":
            if evt.type == pg.MOUSEBUTTONDOWN:
                x, y = evt.pos
                if y>70 and y<97:
                    arr = setGame(1)
                    r = 1
                elif y>100 and y<127:
                    arr = setGame(2)
                    r = 2
                elif y>130 and y<157:
                    arr = setGame(3)
                    r = 3
                elif y>160 and y<197:
                    arr = setGame(4)
                    r = 4
                elif y>190 and y<227:
                    arr = setGame(5)
                    r = 5
        if complete == "success":
            if evt.type == pg.MOUSEBUTTONDOWN:
                x, y = evt.pos
                if y>height//2+137 and y<height//2+177:
                    complete = "menu"
    if running:
        if complete == "menu":
            screen.fill((0,0,0))
            t1 = font.render(f"MENU", True, (255,255,255))
            t2 = font.render(f"EASY", True, (255,255,255))
            t3 = font.render(f"MEDIUM", True, (255,255,255))
            t4 = font.render(f"HARD", True, (255,255,255))
            t5 = font.render(f"INTENSE", True, (255,255,255))
            t6 = font.render(f"IMPOSSIBLE", True, (255,255,255))
            screen.blit(t1, (25,34))
            pg.draw.rect(screen, (255,255,255), (25, 65, 50, 2))
            screen.blit(t2, (25,70))
            screen.blit(t3, (25,100))
            screen.blit(t4, (25,130))
            screen.blit(t5, (25,160))
            screen.blit(t6, (25,190))
            pg.display.update()
        elif complete == "playing":
            change()
            drawGrid()
            pg.display.update()
            endGame = int(time.time())
        elif complete=="success":
            screen.fill((0,0,0))
            pre = int(open(".\\assets\\highScore.txt", "r").read().split("\n")[r-1])
            cnt = int(endGame-startGame)
            if cnt>pre and pre!=0:
                timeR = font.render(f"CURRENT SCORE : {int(endGame-startGame)} SECS", True, (255,255,255))
                tr1 = timeR.get_rect()
                tr1.center = (width//2, height//2+90)
                t2 = font.render(f"{pre} SEC", True, (255,255,255))
                t_2 = t3.get_rect()
                t_2.center = (width//2, height//2+30)
                t1 = font.render(f"PREVIOUS HIGH SCORE WAS", True, (255,255,255))
                t_1 = t1.get_rect()
                t_1.center = (width//2, height//2-30)
                screen.blit(timeR, tr1)
                screen.blit(t1, t_1)
                screen.blit(t2, t_2)
            else:
                t = font.render(f"{cnt} SEC", True, (255, 255, 255))
                t_ = t.get_rect()
                t_.center = (width//2, height//2+30)
                pre = open(".\\assets\\highScore.txt", "r").read().split("\n")
                pre[r-1] = cnt
                pre = "\n".join([str(i) for i in pre])
                f = open(".\\assets\\highScore.txt", "w")
                f.write(pre)
                f.close()
                t1 = font.render(f"NEW HIGH SCORE", True, (255,255,255))
                t_1 = t1.get_rect()
                t_1.center = (width//2, height//2-30)
                screen.blit(t, t_)
                screen.blit(t1, t_1)
            play_again = font.render("PLAY AGAIN", True, (255,255,255))
            pa = play_again.get_rect()
            pa.center = (width//2, height//2+150)
            screen.blit(play_again, pa)
            pg.display.update()