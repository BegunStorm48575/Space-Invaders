import pygame

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

def player (x, y):
     screen.blit(playerImg, (x, y))

# game loop
running = True

while running:
    screen.fill((77, 66, 66))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player(playerX, playerY)

    
 
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
    print(playerX)
    player(playerX, playerY)

    # update screen
    pygame.display.update()
    









