import pygame
import random
 # initialize the pygame
pygame.init()

 # screen
screen = pygame.display.set_mode ((800,600))

 # Tittle
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480

playerX_change = 0

enemyImg = pygame.image.load("alien-pixelated-shape-of-a-digital-game.png")

enemyX = random.randint(0,800)
enemyY = random.randint(50,150)

enemyX_change = 0.2
enemyY_change = 100


def enemy (x, y):
     screen.blit(enemyImg, (x, y))

def player (x, y):
     screen.blit(playerImg, (x, y))

# game loop
running = True

while running:
    screen.fill((77, 66, 66))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Handles the key down event
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change -= 0.1
        elif event.key == pygame.K_RIGHT:
            playerX_change += 0.1

    # Handles the key up event
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # update playerX location
    playerX += playerX_change
    player(playerX, playerY)

    enemyX += enemyX_change
    if enemyX <=0:
        enemyY_change +=0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change
    
    enemy(enemyX, enemyY)
    

    # update screen
    pygame.display.update()
    









