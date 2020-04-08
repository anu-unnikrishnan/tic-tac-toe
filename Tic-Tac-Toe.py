#play Tic-Tac-Toe with two human players

#print board
def printboard(board, n):
    print("\n")
    for i in range(0, n*n):
        print("[", board[i], "]", end = " ")
        if i != 0 and (i+1) % n == 0:
            print("\n")

#check if there are empty spaces left on board
def emptyspaces(board, n):
    spaceflag = 0
    for i in range(0, n*n):
        if board[i] == ' ':
            spaceflag = 1
    return spaceflag

#check if any row is full of Xs/Os
def checkrows(board, n, turn):
    for i in range(0, n*n, n):
        checkflag = 0
        for j in range(i, i+n):
            if turn == 0 and board[j] == 'X':
                checkflag += 1
            elif turn == 1 and board[j] == 'O':
                checkflag += 1
        if checkflag == n:
            return 1
    return 0

#check if any col is full of Xs/Os
def checkcols(board, n, turn):
    for i in range(0, n):
        checkflag = 0
        for j in range(i, i+n*(n-1)+1, n):
            if turn == 0 and board[j] == 'X':
                checkflag += 1
            elif turn == 1 and board[j] == 'O':
                checkflag += 1
        if checkflag == n:
            return 1
    return 0

#check if any diagonal is full of Xs/Os
def checkdiags(board, n, turn):
    #left-up to right-down diagonal
    checkflag = 0
    for i in range(0, n*n, n+1):
        if turn == 0 and board[i] == 'X':
            checkflag += 1
        elif turn == 1 and board[i] == 'O':
            checkflag += 1
    if checkflag == n:
        return 1
    #left-down to right-up diagonal
    else:
        checkflag = 0
        for i in range(n-1, n*(n-1)+1, n-1):
            if turn == 0 and board[i] == 'X':
                checkflag += 1
            elif turn == 1 and board[i] == 'O':
                checkflag += 1
        if checkflag == n:
            return 1
        else:
            return 0

#returns +1 if X has won, -1 if O has won, 0 if draw
def checkwin(board, n):
    #check if X has won (player 1)
    if checkrows(board, n, 0) == 1 or checkcols(board, n, 0) == 1 or checkdiags(board, n, 0) == 1:
        return 1
    #check if O has won (player 2)
    elif checkrows(board, n, 1) == 1 or checkcols(board, n, 1) == 1 or checkdiags(board, n, 1) == 1:
        return -1
    #check if draw i.e. no blank spaces left but neither X/O has won
    elif emptyspaces(board, n) == 0:
        return 0

#check if move is valid i.e. on the board and blank
def isvalid(move):
    if move >= 0 and move < n*n:
        if board[move] == ' ':
            return 1
    return 0

#let's store the board as an array of length n*n
#each element is either X or O or [blank]
n = 3
choice = 'y'

#play as many games as the players want
while choice == 'y':

    print("\n-----------------------\nWelcome to Tic-Tac-Toe!\n-----------------------")
    board = []
    #print blank board
    for i in range(0, n*n):
        board.append(' ')
    printboard(board, n)

    #keep going while there are still empty spaces on board
    while emptyspaces(board, n) == 1:
        
        validflag = 0
        #keep going until player 1 enters a valid move
        while validflag == 0:
              move = eval(input("\nPlayer 1 (X), enter your move : "))
              if isvalid(move) == 1:
                validflag = 1
              else:
                print("Invalid move. Try again!")
        #play X there
        board[move] = 'X'
        printboard(board, n)

        #check if anyone has won yet
        if checkwin(board, n) == 1:
            print("Player 1 has won!\n")
            break
        elif checkwin(board, n) == -1:
            print("Player 2 has won!\n")
            break
        elif checkwin(board, n) == 0:
            print("It's a draw!\n")
            break

        #keep going until player 2 enters a valid move
        validflag = 0
        while validflag == 0:
            move = eval(input("\nPlayer 2 (O), enter your move : "))
            if isvalid(move) == 1:
                validflag = 1
            else:
                print("Invalid move. Try again!")
        #play O there
        board[move] = 'O'
        printboard(board, n)

        #check if anyone has won yet
        if checkwin(board, n) == 1:
            print("Player 1 has won!\n")
            break
        elif checkwin(board, n) == -1:
            print("Player 2 has won!\n")
            break
        elif checkwin(board, n) == 0:
            print("It's a draw!\n")
            break
                
    choice = input("Want another go? (y/n) ")



