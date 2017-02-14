from msvcrt import getch
initPos=54
loss=False
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
            moveVert(space,key)
        elif key == 97 or key == 100: #left(a) is 97, right(d) is 100
            moveHor(space,key)
    print()
    print('GAME OVER')
def moveVert(x,y):
    global initPos
    if y == 119:
        up=True
    elif y == 115:
        up=False
    if up==True:
        x[initPos]='   '
        initPos-=10
        x[initPos]=' x '
        checkLoss(initPos)
    if up==False:
        x[initPos]='   '
        initPos+=10
        x[initPos]=' x '
        checkLoss(initPos)
    board(x)

def moveHor(x,y):
    global initPos
    if y == 97:
        left=True
    elif y == 100:
        left=False
    if left==True:
        x[initPos]='   '
        initPos-=1
        x[initPos]=' x '
        checkLoss(initPos)
    if left==False:
        x[initPos]='   '
        initPos+=1
        x[initPos]=' x '
        checkLoss(initPos)
    board(x)
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

    
    
    
