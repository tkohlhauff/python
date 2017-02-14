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
        if key == 224:
            key== ord(getch())
            if key == 80 or key == 72: #down is 80, up is 72
                moveVert(space,key)
            elif key == 75 or key == 77: #left is 75, right is 77
                moveHor(space,key)
def moveVert(x,y):
    initSpace=54
    if y == 80:
        up=False
    elif y == 72:
        up=True
    if up==True:
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

    
    
    
