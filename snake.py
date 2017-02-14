from msvcrt import getch
def main():
    space=['   ']
    space*=101
    print("Welcome to Snake")
    space[54]=' x '
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
    while True:
        key = ord(getch())
        if key == 119 or key == 115: #up(w)is 119, down(s) is 115
            moveVert(space,key)
        elif key == 97 or key == 100: #left(a) is 97, right(d) is 100
            moveHor(space,key)
def moveVert(x,y):
    print('here')
    initSpace=54
    if y == 119:
        up=False
    elif y == 115:
        up=True
    if up==True:
        print('here')
        initSpace+=10
        x[initSpace]=' x '
    board(x)    
        

def clear():
    import os
    if os.name in "posix":
        os.system('clear')
    elif os.name in ['nt','dos','ce']:
        os.system('CLS')

    
main()

    
    
    
