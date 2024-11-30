import random
board = ["_", "_","_",
         "_", "_", "_",
         "_", "_", "_"]
currentplayer = "X"
winner = None
gameRunning =True

#printing the game board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("_________")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("_________")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("_________")
printBoard(board)

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "_":
        board[inp-1] = currentplayer
    else:
        print("OOps player is already in that spot!")

#check for win or tie again
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
       winner = board[0]
       return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
       winner = board[1]
       return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
       winner = board[0]
       return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
       winner = board[2]
       return True
def checkTie(board):
    global gameRunning
    if "_" not in board:
        printBoard(board)
        print("it is a tie!")
        gameRunning = False
def checkWin():
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
#switch player
def switchPlayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"  
#computer
def computer(board):
    while currentplayer == "O":
        position = random.randint(0,8)
        if board[position] == "_":
            board[position] = "O"
            switchPlayer()
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
