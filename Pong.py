import pygame
import time
pygame.init()
canvas = pygame.display.set_mode((1080,720))
pygame.display.set_caption('Pong Ultimate')
players = 1
x = 250
y = 250
yy = 250
yyy = 250
speedx = 10
speedy = 5
paddle_speed = 6
CPU,Player = 0,0
win_message = pygame.font.Font('freesansbold.ttf', 32)
time.sleep(3)
count = 1
while True:
    if x < 95 and y in range(yy-10, yy+80): speedx *= -1
    if x > 985 and y in range(yyy - 10, yyy+80): speedx *= -1
    if x == 985 and y == 250: speedx *= -1
    if y == 710: speedy *= -1
    if y == 10: speedy *= -1
    if x == 1070:
        Player += 1
        time.sleep(2)
        break
    if x == 10:
        CPU += 1
        time.sleep(2)
        break
    x += speedx
    y += speedy

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if players == 2:
        if keys[pygame.K_UP] and yyy > 0:
            yyy -= paddle_speed
        if keys[pygame.K_DOWN] and yyy < 640:
            yyy += paddle_speed
    else:
        yyy = y

    if keys[pygame.K_w] and yy > 0:
        yy -= paddle_speed
    if keys[pygame.K_s] and yy < 640:
        yy += paddle_speed
    canvas.fill((0,0,0))
    pygame.draw.rect(canvas, (255,255,255), (75,yy,20,80))
    pygame.draw.circle(canvas, (255,0,0),(x,y),20)
    pygame.draw.rect(canvas, (255,255,255), (985, yyy, 20, 80))
    pygame.display.update()
    if CPU == 10 or Player == 10:
        break
    count = count + 1

pygame.quit()
