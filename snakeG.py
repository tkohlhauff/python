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
currX=400
currY=400
size=(800,800)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
rect=pygame.Rect(400,400,HEIGHT,HEIGHT)
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
    #draws the snake
    for x in last:
        rect=pygame.draw.rect(screen,WHITE,(x[0],x[1],HEIGHT,HEIGHT),0)
    #draws the block needed to be picked up
    ranBlock=pygame.draw.rect(screen,WHITE,(ranx,rany,HEIGHT,HEIGHT),0)
    #sets movement determined by last input
    if move=='up':
        currY-=HEIGHT
    elif move=='down':
        currY+=HEIGHT
    elif move=='left':
        currX-=HEIGHT
    elif move=='right':
        currX+=HEIGHT
    #create list for last position
    lastXY=[]
    lastXY.append(currX)
    lastXY.append(currY)
    #reverse list to set last movement to first position
    lastXY.reverse()
    lastXY.reverse()
    #append last list with both positions
    last.append(lastXY)
    #delete extra movements from last
    if len(last)>collected:
        del last[0]
    #check collision with block to pick up
    if rect.colliderect(ranBlock):
        collect=False
        collected+=1
        #speed up game every 3 pick ups
        if collected%3==0:
            fps+=3
    #check wall collisions
    if -15>currX or currX>1015 or -15>currY or currY>1015:
        pygame.quit()
    #check collision with self
    for x in last[:-1]:
        if x==lastXY:
            pygame.quit()
#create position for random block
def ranBlock():
    global ranx, rany, collect
    collect=True
    ranx=random.randint(0,485)
    rany=random.randint(0,485)
   
        

        
main()
