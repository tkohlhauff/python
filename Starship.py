import pygame
import random

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
topCount = False
an = 0
treantIdle=0
treantCount=0
playerImg = pygame.image.load('Wizard-front-2.png')

pressed=False

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
    global lastDir, topCount, an,treantIdle,treantCount
    global x, y, x_change, y_change, sprites,pressed
    #Checks direction from keypressed and moves count for sprite animation
    if topCount:
        an -= 1
    else:
        an += 1
    if an==2:
        topCount=True
    elif an==0:
        topCount=False
    # Movement for the player
    if x + x_change >= 0 and x + x_change <= display_width - player_width:
            x += x_change
    if y + y_change >= 0 and y + y_change <= display_height - player_height:
        y += y_change

    #check for key change during animation as well as let go of key
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pressed=True
                lastDir=0
            if event.key == pygame.K_UP:
                pressed=True
                lastDir=1
            if event.key == pygame.K_RIGHT:
                pressed=True
                lastDir=2
            if event.key == pygame.K_DOWN:
                pressed=True
                lastDir = 3
        if event.type==pygame.KEYUP:
            pressed=False
    treantIdle+=1
    if treantIdle%33==0:
        treantCount=1
    if treantIdle%70==0:
        treantCount=0
    draw()
##    #Draws the sprites based on direction and change in x,y position      
##    gameDisplay.fill(white)
##    if lastDir == 0:
##        player(sprites[2][an],x,y)
##        
##    elif lastDir == 1:
##        player(sprites[0][an],x,y)
##        
##    elif lastDir == 2:
##        player(sprites[3][an],x,y)
##
##    elif lastDir == 3:
##        player(sprites[1][an],x,y)
##    
##    pygame.display.update()
##    clock.tick(30)
def draw():
    #Draws the sprites based on direction and change in x,y position      
    gameDisplay.fill(white)
    treant(treantSprite[treantCount])
    if lastDir == 0:
        player(sprites[2][an],x,y)
        
    elif lastDir == 1:
        player(sprites[0][an],x,y)
        
    elif lastDir == 2:
        player(sprites[3][an],x,y)

    elif lastDir == 3:
        player(sprites[1][an],x,y)
    
    pygame.display.update()
    clock.tick(30)
    
def game_loop():
    global lastDir, x_change, y_change, pressed,treantIdle,treantCount

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
                    pressed=True
                    lastDir=0
                if event.key == pygame.K_UP:
                    pressed=True
                    lastDir=1
                if event.key == pygame.K_RIGHT:
                    pressed=True
                    lastDir=2
                if event.key == pygame.K_DOWN:
                    pressed=True
                    lastDir = 3
        #use a loop for button pressses, needed for long presses
            while pressed==True:
                if lastDir == 0:
                    x_change = -5
                    movement()
                    x_change=0
                if lastDir == 1:
                    y_change = -5
                    movement()
                    y_change=0 

                if lastDir == 2:
                    x_change = 5
                    movement()
                    x_change=0 

                if lastDir == 3:
                    y_change = 5
                    movement()
                    y_change=0
        treantIdle+=1
        if treantIdle%33==0:
            treantCount=1
        if treantIdle%70==0:
            treantCount=0
        draw()
    
   

                        

        

game_loop()
pygame.quit()
quit()





'''
******************************************** NOTES ********************************************
Animation works now, except you cant hold down button and switch directions immediately 
'''
