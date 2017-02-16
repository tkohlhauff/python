from msvcrt import getch
import time
initPos=54
loss=False
pos='down'
def main():
    global initPos
    global pos
    space=['   ']
    space*=101
    print("Welcome to Snake")
    space[initPos]=' x '
    for x in range(10):
        space[x]=' - '
        space[x*10]=' - '
        space[x*10+9]=' - '
        space[100-x]=' - '
    z=0
    for x in range(10):
        print()
        for y in range(10):
            print(space[z], end='')
            z+=1
    movement(space,pos)

def reDraw(space):
    clear()
    z=0
    for x in range(10):
        print()
        for y in range(10):
            print(space[z], end='')
            z+=1
def checkMove(key):
    if key == 119 or key == 115: #up(w)is 119, down(s) is 115
        moveVert(key)
    elif key == 97 or key == 100: #left(a) is 97, right(d) is 100
        moveHor(key)
def moveVert(x):
    global pos
    if x == 119:
        up=True
    elif x == 115:
        up=False
    if up==True:
        pos='up'
    elif up==False:
        pos='down'

def moveHor(x):
    global pos
    if x == 97:
        left=True
    elif x == 100:
        left=False
    if left==True:
        pos='left'
    elif left==False:
        pos='right'

def movement(space,pos):
    global initPos
    while pos=='left' and loss==False:
        key = ord(getch())
        time.sleep(1)
        space[initPos]='   '
        initPos-=1
        space[initPos]=' x '
        checkLoss(initPos)
        reDraw(space)
    while pos=='right' and loss==False:
        key = ord(getch())
        time.sleep(1)
        space[initPos]='   '
        initPos+=1
        space[initPos]=' x '
        checkLoss(initPos)
        reDraw(space)
    while pos=='up' and loss==False:
        key = ord(getch())
        checkMove(key)
        time.sleep(1)
        space[initPos]='   '
        initPos-=10
        space[initPos]=' x '
        checkLoss(initPos)
        reDraw(space)
    while pos=='down' and loss==False:
        key = ord(getch())
        time.sleep(1)
        space[initPos]='   '
        initPos+=10
        space[initPos]=' x '
        checkMove(key)
        checkLoss(initPos)
        reDraw(space)
def checkLoss(x):
    global loss
    if x<11 or x>89:
        loss=True
    
        

def clear():
    import os
    if os.name in "posix":
        os.system('clear')
    elif os.name in ['nt','dos','ce']:
        os.system('CLS')

    
main()
