import pygame
import time
import random
from pygame import Rect

green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
xcoord = 0
ycoord = 0
x = 190
y = 190
direction = "none"
counter = 0
coordlistx = [x]
coordlisty = [y]
bodylistx = []
bodylisty = []

pygame.init()
pygame.font.init()

def makecoord():
    xval = (round((random.random() * 380))//20) * 20 + 10
    return xval

dis = pygame.display.set_mode((405, 405))
pygame.display.set_caption('Snake')
font = pygame.font.SysFont('Arial', 50)
font2 = pygame.font.SysFont('Comic Sans MS', 20)
game_over = False
clock = pygame.time.Clock()
fcx = makecoord()
fcy = makecoord()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ycoord = -20
                xcoord = 0
            elif event.key == pygame.K_a:
                xcoord = -20
                ycoord = 0
            elif event.key == pygame.K_s:
                ycoord = 20
                xcoord = 0
            elif event.key == pygame.K_d:
                xcoord = 20
                ycoord = 0

    x += xcoord
    y += ycoord

    bodylistx.clear()
    bodylisty.clear()
    
    coordlistx.append(x)
    coordlisty.append(y)

    scoreboard = font2.render(str(counter), False, white)
    dis.blit(scoreboard, (30, 30))
    pygame.display.update()

    if x < 0 or y < 0 or x > 390 or y > 390 or x in bodylistx and y in bodylisty:
        texty = font.render('You Lost!', False, white)
        texty2 = font2.render('Press W to continue', False, white)
        dis.blit(texty, (100,165))
        dis.blit(texty2, (110, 220))
        if pygame.key.get_pressed()[pygame.K_w]:
            x = 190
            y = 190
            counter = 0
            xcoord = 0
            ycoord = 0
            coordlistx = [x]
            coordlisty = [y]
            bodylistx.clear()
            bodylisty.clear()
            fcx = makecoord()
            fcy = makecoord()
        pygame.display.update()
    else:
        dis.fill((0, 0, 0))
        if x == fcx and y == fcy:
            fcx = makecoord()
            fcy = makecoord()
            counter += 1

        pygame.draw.rect(dis, green, [x, y, 20, 20])
        pygame.draw.rect(dis, red, [fcx, fcy, 20, 20])

        coordlistx.reverse()
        coordlisty.reverse()

        for z in range(counter+1):
            pygame.draw.rect(dis, green, [coordlistx[z], coordlisty[z], 20, 20])
            if z > 0:
                bodylistx.append(coordlistx[z])
                bodylisty.append(coordlisty[z])

        coordlistx.reverse()
        coordlisty.reverse()

        clock.tick(10)
        pygame.display.update()


pygame.quit()
quit()

