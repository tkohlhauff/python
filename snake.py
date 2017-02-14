from msvcrt import getch
import time
initPos=54
loss=False
pos='down'
def main():
    global initPos
    space=['   ']
    space*=101
    print("Welcome to Snake")
    space[initPos]=' x '
    for x in range(10):
        space[x]=' - '
        space[x*10]=' - '
        space[x*10+9]=' - '
        space[100-x]=' - '
    board(space)

def board(space):
    global pos
    clear()
    z=0
    for x in range(10):
        print()
        for y in range(10):
            print(space[z], end='')
            z+=1
    move(space)
def move(space):
    while loss==False:
        key = ord(getch())
        if key == 119 or key == 115: #up(w)is 119, down(s) is 115
            moveVert(key,space)
        elif key == 97 or key == 100: #left(a) is 97, right(d) is 100
            moveHor(key,space)
        
def moveVert(x,y):
    global initPos
    global pos
    if x == 119:
        up=True
    elif x == 115:
        up=False
    if up==True:
        pos='up'
    elif up==False:
        pos='down'
    movement(y,pos)

def moveHor(x,y):
    global pos
    if x == 97:
        left=True
    elif x == 100:
        left=False
    if left==True:
        pos='left'
    elif left==False:
        pos='right'
        
    movement(y,pos)

def movement(space,pos):
    global initPos
    space[initPos]='   '
    if pos=='left':
        time.sleep(1)
        initPos-=1
    elif pos=='right':
        time.sleep(1)
        initPos+=1
    elif pos=='up':
        time.sleep(1)
        initPos-=10
    elif pos=='down':
        time.sleep(1)
        initPos+=10
    space[initPos]=' x '
    checkLoss(initPos)
    board(space)
def checkLoss(x):
    global loss
    if x<11:
        loss=True
    elif x>89:
        loss=True
    
        

def clear():
    import os
    if os.name in "posix":
        os.system('clear')
    elif os.name in ['nt','dos','ce']:
        os.system('CLS')

    
main()

    
    
    
