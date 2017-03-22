import pygame
import random
import math

pygame.init()

display_width = 1200
display_height = 800
player_height = 32
player_width = 32

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('StarShooter')
clock = pygame.time.Clock()

#value for player position
x = (display_width * 0.45)
y = (display_height * 0.8)
randx=0
randy=0

#value for speed/direction
x_change = 0
y_change = 0

lastDir = 3 # 0 = left, 1 = up, 2 = right, 3 = down
# Sprite animation step count once it reaches three set topCount to true and go down
stepCount = 0
an = 0
treantIdle=0
treantCount=0
playerImg = pygame.image.load('Wizard-front-2.png')
pygame.key.set_repeat(33, 33)

pressed=False
left=False
right=False
up=False
down=False
# Arrays containing sprite animations; 0 is up, 1 is Down, 2 is left, 3 is right
sprites=[['Wizard-back-1.png','Wizard-back-2.png','Wizard-back-3.png'],['Wizard-front-1.png','Wizard-front-2.png','Wizard-front-3.png'],
         ['Wizard-left-1.png','Wizard-left-2.png','Wizard-left-3.png'],['Wizard-right-1.png','Wizard-right-2.png','Wizard-right-3.png']]
treantSprite=['Treent-front-1.png','Treent-front-2.png']
def treant(img):
    treantImg=pygame.image.load(img)
    gameDisplay.blit(treantImg,(400,350))
def player(img,x,y):
    playerImg = pygame.image.load(img)
    gameDisplay.blit(playerImg,(x,y))

def movement():
    global lastDir, stepCount, an,treantIdle,treantCount
    global x, y, x_change, y_change, sprites,pressed
    global right,left,up,down
    #Count for walk animation
    stepCount+=1
    if stepCount==3:
        an=0
    if stepCount==9:
        an=1
    if stepCount==12:
        an=2
        stepCount=0
    # Movement for the player
    if x + x_change >= 0 and x + x_change <= display_width - player_width:
            x += x_change
    if y + y_change >= 0 and y + y_change <= display_height - player_height:
        y += y_change

    #check for key change during animation as well as let go of key
        
    treantIdle+=1
    if treantIdle==30:
        treantCount=1
    if treantIdle==60:
        treantCount=0
        treantIdle=0
    draw()
def draw():
        
    #background
    back = pygame.image.load('Sand-5.png').convert()
    for i in range(math.floor(display_width / 32) + 1):
        for z in range(math.floor(display_height / 32) + 1):
            gameDisplay.blit(back,(i*32,z*32))
    #Draws the sprites based on direction and change in x,y position  
    treant(treantSprite[treantCount])

    if lastDir==0:
        player(sprites[2][an],x,y)
    if lastDir==1:
        player(sprites[0][an],x,y)
    if lastDir==2:
        player(sprites[3][an],x,y)
    if lastDir==3:
        player(sprites[1][an],x,y)
    
    pygame.display.update()
    clock.tick(30)
    
def game_loop():
    global lastDir, x_change, y_change, pressed,treantIdle,treantCount
    global right,left,up,down

    # Game close boolean
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
        #Checks the button press and determines the direction, 0 left, 1 up, 2 right, 3 down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    movement()
                    x_change=0
                    lastDir=0
                if event.key == pygame.K_UP:
                    y_change = -5
                    movement()
                    y_change=0
                    lastDir=1
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    movement()
                    x_change=0
                    lastDir=2
                if event.key == pygame.K_DOWN:
                    y_change = 5
                    movement()
                    y_change=0
                    lastDir=3
        #use a loop for button pressses, needed for long presses
##            while pressed==True:
##                if left:
##                    x_change = -5
##                    movement()
##                    x_change=0
##                    lastDir=0
##                elif up:
##                    y_change = -5
##                    movement()
##                    y_change=0 
##                    lastDir=1
##                elif right:
##                    x_change = 5
##                    movement()
##                    x_change=0 
##                    lastDir=2
##                elif down:
##                    y_change = 5
##                    movement()
##                    y_change=0
##                    lastDir=3
        treantIdle+=1
        if treantIdle==30:
            treantCount=1
        if treantIdle==60:
            treantCount=0
            treantIdle=0
        draw()
    
   

                        

        

game_loop()
pygame.quit()
quit()





'''
******************************************** NOTES ********************************************
Animation works now, except you cant hold down button and switch directions immediately 
'''
