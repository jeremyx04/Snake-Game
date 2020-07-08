import pygame
import time
from snake import Snake
from food import Food
def drawmap():
    for i in range(16):
        for j in range(16):
            if (i + j) % 2 == 0:
                pygame.draw.rect(win,purple1,(i*50,j*50,50,50))
            else:
                pygame.draw.rect(win,purple2,(i*50,j*50,50,50))
def showScore():
    win.fill((255,255,255),(800,0,200,800)) 
    text = font.render('Score: ' + str(player.score), True, pink)
    textRect = text.get_rect()
    textRect.center = (900,250)
    win.blit(text,textRect)
pygame.init()
win = pygame.display.set_mode((1000,800))
pygame.display.set_caption('SNAKE')
purple1 = (156, 136, 255)
purple2 = (140, 122, 230)
pink = (253,121,168)
blue = (10, 189, 227)
font = pygame.font.Font(pygame.font.get_default_font(),30)
win.fill((255,255,255),(800,0,200,800))
game = 1
player = Snake()
start = 0
food = Food(player.x,player.y)
showScore()
while game: 
    pygame.display.update()
    drawmap()
    pygame.draw.rect(win,blue,(food.x*50,food.y*50,50,50))
    for i in range(len(player.pos)):
        pygame.draw.rect(win,pink,(player.pos[i][0]*50,player.pos[i][1]*50,50,50))
    if start:
        tempx = player.x
        tempy = player.y
        player.move()
        if player.x == food.x and player.y == food.y:
            food.eaten = 1
            player.score+=10
            player.size+=1       
            player.pos.append((tempx,tempy)) 
            showScore()
        if len(player.pos) > 2:
            for i in range(len(player.pos)-1):
                if player.x == player.pos[i+1][0] and player.y == player.pos[i+1][1]:
                    game = 0
    if player.x >= 16 or player.y >= 16 or player.x < 0 or player.y < 0:
        game = 0
    if food.eaten:
        food = Food(player.x,player.y)
    pygame.display.update()
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player.direction != 'd':
                player.direction = 'u'
                start = 1
            elif event.key == pygame.K_DOWN and player.direction !='u':
                player.direction = 'd'
                start = 1
            elif event.key == pygame.K_LEFT and player.direction !='r':
                player.direction = 'l'
                start = 1
            elif event.key == pygame.K_RIGHT and player.direction !='l':
                player.direction = 'r'
                start = 1
    if not game:
        time.sleep(2)
print('Score:',player.score)
exit()
