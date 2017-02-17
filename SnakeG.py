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
currX=500
currY=500
size=(1000,1000)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
rect=pygame.Rect(500,500,HEIGHT,HEIGHT)
move='down'
collected=1
last=[[currX,currY]]
fps=15
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
        if not collect:
            ranBlock()
        chkMove(move)
        #updates screen
        pygame.display.flip()
        #fps

        clock.tick_busy_loop(fps)
    pygame.quit()


        
def chkMove(move):
    global currY,currX,collected,rect,collect,fps
    for x in last:
        rect=pygame.draw.rect(screen,WHITE,(x[0],x[1],HEIGHT,HEIGHT),0)
    ranBlock=pygame.draw.rect(screen,WHITE,(ranx,rany,HEIGHT,HEIGHT),0)
    if move=='up':
        currY-=HEIGHT
    elif move=='down':
        currY+=HEIGHT
    elif move=='left':
        currX-=HEIGHT
    elif move=='right':
        currX+=HEIGHT
    lastXY=[]
    lastXY.append(currX)
    lastXY.append(currY)
    lastXY.reverse()
    lastXY.reverse()
    last.append(lastXY)
    if len(last)>collected:
        del last[0]
    if rect.colliderect(ranBlock):
        collect=False
        collected+=1
        if collected%3==0:
            fps+=3
    if -15>currX or currX>1015 or -15>currY or currY>1015:
        pygame.quit()
    for x in last[:-1]:
        if x==lastXY:
            pygame.quit()
def ranBlock():
    global ranx, rany, collect
    collect=True
    ranx=random.randint(0,485)
    rany=random.randint(0,485)
   
        

        
main()
