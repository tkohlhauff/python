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
        if selection==1 and space[selection-1]=='     ':
            if turnX==True:
                space[0]=x
                redrawBoard(space)
                turnX=False
            else:
                space[0]=o
                redrawBoard(space)
                turnX=True
        if selection==2 and space[selection-1]=='     ':
            if turnX==True:
                space[1]=x
                redrawBoard(space)
                turnX=False
            else:
                space[1]=o
                redrawBoard(space)
                turnX=True
        if selection==3 and space[selection-1]=='     ':
            if turnX==True:
                space[2]=x
                redrawBoard(space)
                turnX=False
            else:
                space[2]=o
                redrawBoard(space)
                turnX=True
        if selection==4 and space[selection-1]=='     ':
            if turnX==True:
                space[3]=x
                redrawBoard(space)
                turnX=False
            else:
                space[3]=o
                redrawBoard(space)
                turnX=True
        if selection==5 and space[selection-1]=='     ':
            if turnX==True:
                space[4]=x
                redrawBoard(space)
                turnX=False
            else:
                space[4]=o
                redrawBoard(space)
                turnX=True
        if selection==6 and space[selection-1]=='     ':
            if turnX==True:
                space[5]=x
                redrawBoard(space)
                turnX=False
            else:
                space[5]=o
                redrawBoard(space)
                turnX=True
        if selection==7 and space[selection-1]=='     ':
            if turnX==True:
                space[6]=x
                redrawBoard(space)
                turnX=False
            else:
                space[6]=o
                redrawBoard(space)
                turnX=True
        if selection==8 and space[selection-1]=='     ':
            if turnX==True:
                space[7]=x
                redrawBoard(space)
                turnX=False
            else:
                space[7]=o
                redrawBoard(space)
                turnX=True
        if selection==9 and space[selection-1]=='     ':
            if turnX==True:
                space[8]=x
                redrawBoard(space)
                turnX=False
            else:
                space[8]=o
                redrawBoard(space)
                turnX=True
        gameOvah=checkWin(space)
        if gameOvah == True:
            selection=input("Would you like to play again?: ")
            if selection in ["yes","y","Yes","Y"]:
                freshBoard()
            else:
                print("Thank you for playing!")
        
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
            print("Congrats",space[0],"you won!")
            return True
        elif space[0] in space[4] and space[0] in space[8]:
            print("Congrats",space[0],"you won!")
            return True
        elif space[0] in space[1] and space[0] in space[2]:
            print("Congrats",space[0],"you won!")
            return True
    if space[1]=="  X  " or space[1]=="  O  ":
        if space[1] in space[4] and space[1] in space[7]:
            print("Congrats",space[1],"you won!")
            return True
    if space[2] =="  X  " or space[2] == "  O  ":
        if space[2] in space[5] and space[2] in space[8]:
            print("Congrats",space[2],"you won!")
            return True
        elif space[2] in space[4] and space[2] in space[6]:
            print("Congrats",space[2],"you won!")
            return True
    if space[3]=="  X  " or space[3]=="  O  ":
        if space[3] in space[4] and space[3] in space[5]:
            print("Congrats",space[3],"you won!")
            return True
    return False
        
def clear():
    import os
    if os.name in "posix":
        os.system('clear')
    elif os.name in ['nt','dos','ce']:
        os.system('CLS')
    
        
main()
