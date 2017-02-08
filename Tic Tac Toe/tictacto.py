def main():
    print("Welcome to tictactoe1")
    print("Use the numbers 1-9 for the space accordingly")
    freshBoard()
def freshBoard():
    space=['     ']
    space*=9
    print(space[0],"|",space[1],"|",space[2])
    print(" --------------------")
    print(space[3],"|",space[4],"|",space[5])
    print(" --------------------")
    print(space[6],"|",space[7],"|",space[8])
    gameMechanics(space)
    
def gameMechanics(space):
    x="  X  "
    o="  O  "
    turnX=True
    gameOvah=False
    while gameOvah==False:
        selection=int(input("Enter the number of the space you would like to mark: "))
        if selection==1:
            if turnX==True:
                space[0]=x
                redrawBoard(space)
                turnX=False
            else:
                space[0]=o
                redrawBoard(space)
                turnX=True
        if selection==2:
            if turnX==True:
                space[1]=x
                redrawBoard(space)
                turnX=False
            else:
                space[1]=o
                redrawBoard(space)
                turnX=True
        if selection==3:
            if turnX==True:
                space[2]=x
                redrawBoard(space)
                turnX=False
            else:
                space[2]=o
                redrawBoard(space)
                turnX=True
        if selection==4:
            if turnX==True:
                space[3]=x
                redrawBoard(space)
                turnX=False
            else:
                space[3]=o
                redrawBoard(space)
                turnX=True
        if selection==5:
            if turnX==True:
                space[4]=x
                redrawBoard(space)
                turnX=False
            else:
                space[4]=o
                redrawBoard(space)
                turnX=True
        if selection==6:
            if turnX==True:
                space[5]=x
                redrawBoard(space)
                turnX=False
            else:
                space[5]=o
                redrawBoard(space)
                turnX=True
        if selection==7:
            if turnX==True:
                space[6]=x
                redrawBoard(space)
                turnX=False
            else:
                space[6]=o
                redrawBoard(space)
                turnX=True
        if selection==8:
            if turnX==True:
                space[7]=x
                redrawBoard(space)
                turnX=False
            else:
                space[7]=o
                redrawBoard(space)
                turnX=True
        if selection==9:
            if turnX==True:
                space[8]=x
                redrawBoard(space)
                turnX=False
            else:
                space[8]=o
                redrawBoard(space)
                turnX=True
        gameOvah=checkWin(space)
def redrawBoard(space):
    clear()
    print(space[0],"|",space[1],"|",space[2])
    print(" --------------------")
    print(space[3],"|",space[4],"|",space[5])
    print(" --------------------")
    print(space[6],"|",space[7],"|",space[8])
def checkWin(space):
    if space[0] =="  X  " or space[0] == "  O  ":
        if space[0] in space[3] and space[0] in space[6]:
            return True
        elif space[0] in space[4] and space[0] in space[8]:
            return True
        elif space[0] in space[1] and space[0] in space[2]:
            return True
    if space[1]=="  X  " or space[1]=="  O  ":
        if space[1] in space[4] and space[1] in space[7]:
            return True
    if space[2] =="  X  " or space[2] == "  O  ":
        if space[2] in space[5] and space[2] in space[8]:
            return True
        elif space[2] in space[4] and space[2] in space[6]:
            return True
    elif space[3]=="  X  " or space[3]=="  O  ":
        if space[3] in space[4] and space[3] in space[5]:
            print("in here")
            return True
    else:
        print("working")
        return False
        
def clear():
    import os
    if os.name in "posix":
        os.system('clear')
    elif os.name in ['nt','dos','ce']:
        os.system('CLS')
    
        
main()
