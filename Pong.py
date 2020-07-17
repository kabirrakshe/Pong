import pygame
import time
pygame.init()
canvas = pygame.display.set_mode((1080,720))
pygame.display.set_caption('Pong Ultimate')
x = 250
y = 250
yy = 250
yyy = 250
speedx = 10
speedy = 5
paddle_speed = 6
CPU,Player = 0,0
font = pygame.font.SysFont('georgiabold', 80, True)
time.sleep(3)
count = 1

contact = pygame.mixer.Sound('Contact.wav')
point = pygame.mixer.Sound('Sosumi.wav')

def Endgame(winner):
    global CPU, Player
    if winner == 'Player':
        Player += 1
    else:
        CPU += 1
    text = font.render(str(Player) + ' : ' + str(CPU), 1, (255,255,255))
    canvas.blit(text, (480, 240))
    pygame.display.update()

while True:
    if x < 95 and y in range(yy-10, yy+80):
        contact.play()
        speedx *= -1
    if x > 985 and y in range(yyy - 10, yyy+80):
        contact.play()
        speedx *= -1
    if y == 710: speedy *= -1
    if y == 10: speedy *= -1
    if x == 1070:
        Endgame('Player')
        point.play()
        x,y = 250, 250
        yy,yyy = 250,250
        speedx, speedy = 10,5
        time.sleep(2)
        continue
    if x == 10:
        Endgame('CPU')
        x,y = 250, 250
        yy,yyy = 250,250
        speedx, speedy = 10,5
        time.sleep(2)
        continue
    x += speedx
    y += speedy

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    yyy = y

    if keys[pygame.K_ESCAPE]:
        break
    if keys[pygame.K_w] and yy > 0:
        yy -= paddle_speed
    if keys[pygame.K_s] and yy < 640:
        yy += paddle_speed
    canvas.fill((0,0,0))
    pygame.draw.rect(canvas, (255,255,255), (75,yy,20,80))
    pygame.draw.circle(canvas, (255,0,0),(x,y),20)
    pygame.draw.rect(canvas, (255,255,255), (985, yyy, 20, 80))
    pygame.display.update()
    if CPU == 10:
        legend = 'CPU'
        break
    if Player == 10:
        legend = 'Player'
        break
    else: legend = "NO_ONE"
    count = count + 1
score = font.render(str(Player) + ' : ' + str(CPU), 1, (255,255,255))
window = font.render('Winner: ' + legend, 1, (255,255,255))
canvas.fill((0,0,0))
canvas.blit(score,(480,240))
canvas.blit(window, (360, 360))
pygame.display.update()
time.sleep(3)
pygame.quit()
