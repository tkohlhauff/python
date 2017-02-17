import pygame
import time
import random
collect=False
pygame.init()
WHITE =( 255, 255, 255)
BLACK =(   0,   0,   0)
HEIGHT=15
ranx=0
rany=0
currX=250
currY=250
lastx=[currX]
lasty=[currY]
size=(500,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
rect=pygame.Rect(250,250,HEIGHT,HEIGHT)
move='down'
collected=1
def main():
    global move
    done = False
    clock= pygame.time.Clock()
    while not done:
        #Get key
        key=pygame.key.get_pressed()
        if key[pygame.K_UP]:
            move='up'
        elif key[pygame.K_DOWN]:
            move='down'
        elif key[pygame.K_LEFT]:
            move='left'
        elif key[pygame.K_RIGHT]:
            move='right'
        #check for quit    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        #draw
        screen.fill(BLACK)
        chkMove()
        if not collect:
            ranBlock()
        block()
        #updates screen
        pygame.display.flip()
        #fps
        clock.tick(8/collected)
    pygame.quit()
def block():
    global rect, collect, collected, currY, currX,lastx,lasty
    for x in range(collected):
        if move=='left':
            pygame.draw.rect(screen,WHITE,(lastx[x],lasty[x],HEIGHT,HEIGHT),0)
        elif move=='right':
            pygame.draw.rect(screen,WHITE,(lastx[x],lasty[x],HEIGHT,HEIGHT),0)
        elif move=='up':
            pygame.draw.rect(screen,WHITE,(lastx[x],lasty[x],HEIGHT,HEIGHT),0)
        elif move=='down':
            pygame.draw.rect(screen,WHITE,(lastx[x],lasty[x],HEIGHT,HEIGHT),0)
    ranBlock=pygame.draw.rect(screen,WHITE,(ranx,rany,HEIGHT,HEIGHT),0)
    if rect.colliderect(ranBlock):
        lastx.append(currX)
        lasty.append(currY)
        collected+=1
        print(collected)
        collect=False
def chkMove():
    global rect,currY,currX,move,lastx,lasty
    for x in range(collected):
        if move=='up':
            rect=rect.move(0,-1*HEIGHT)
            currY-=HEIGHT
        elif move=='down':
            rect=rect.move(0,HEIGHT)
            currY+=HEIGHT
        elif move=='left':
            rect=rect.move(-1*HEIGHT,0)
            currX-=HEIGHT
        elif move=='right':
            rect=rect.move(HEIGHT,0)
            currX+=HEIGHT
        lastx[x]=currX
        lasty[x]=currY
    print(lastx)
    if -10>rect.top or rect.bottom>515 or -10>rect.left or rect.right>515:
        pygame.quit()
def ranBlock():
    global ranx, rany, collect
    collect=True
    ranx=random.randint(0,485)
    rany=random.randint(0,485)
   
        

        
main()
