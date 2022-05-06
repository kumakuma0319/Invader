from re import X
import pygame
from pygame import mixer
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
# screen.fill((150, 150, 150))
pygame.display.set_caption('Invaders Game')

# player
playerImg = pygame.image.load('player.png')
playerX, playerY = 370, 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 4, 40

# Score
score_value = 0

def player(x, y):
    screen.blit(playerImg, (x,y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))

    # font = pygame.font.SysFont(None, 80)
    # message = font.render('Hello World', False, (255, 255, 255))
    # screen.blit(message, (20, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            # if event.key == pygame.K_SPACE:
                # if bullet_state is 'ready':
                    # bulletX = playerX
                    # fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    

    #Enemy
    if enemyY > 440:
        break
    enemyX += enemyX_change
    if enemyX <= 0: #左端に来たら
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >=736: #右端に来たら
        enemyX_change = -4
        enemyY += enemyY_change

    #Score
    font = pygame.font.SysFont(None, 32) # フォントの作成　Noneはデフォルトのfreesansbold.ttf
    score = font.render(f"Score : {str(score_value)}", True, (255,255,255)) # テキストを描画したSurfaceの作成
    screen.blit(score, (20,50))

    player(playerX , playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()