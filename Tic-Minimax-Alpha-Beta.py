def printboard(board, n):
    print("\n")
    for i in range(0, n*n):
        print("[", board[i], "]", end = " ")
        if i != 0 and (i+1) % n == 0:
            print("\n")

def emptyspaces(board, n):
    spaceflag = 0
    for i in range(0, n*n):
        if board[i] == ' ':
            spaceflag = 1
    return spaceflag

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

def checkcols(board, n, turn):
    for i in range(0, n): #i goes from 0 to 3 in steps of 1
        checkflag = 0
        for j in range(i, i+n*(n-1)+1, n):
            if turn == 0 and board[j] == 'X':
                checkflag += 1
            elif turn == 1 and board[j] == 'O':
                checkflag += 1
        if checkflag == n:
            return 1
    return 0

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

#returns -1 if X has won, +1 if O has won, 0 if draw
def checkwin(board, n):
    #check if O has won (computer)
    if checkrows(board, n, 1) == 1 or checkcols(board, n, 1) == 1 or checkdiags(board, n, 1) == 1:
        return 1
    #check if X has won (player)
    elif checkrows(board, n, 0) == 1 or checkcols(board, n, 0) == 1 or checkdiags(board, n, 0) == 1:
        return -1
    #check if draw i.e. no blank spaces left but neither X/O has won
    elif emptyspaces(board, n) == 0:
        return 0
    #otherwise, no one has won
    else:
        return -5

def isvalid(move):
    if move >= 0 and move < n*n:
        if board[move] == ' ':
            return 1
    return 0

#return score and index for best move
def getcomputermove(board, n, depth, ismax, index, alpha, beta):
    
    if checkwin(board, n) == +1 or checkwin(board, n) == -1 or checkwin(board, n) == 0:
        score = checkwin(board, n)
        bestmove = [score, index]
        return bestmove
    
    if ismax == True:
        score = -5
        for i in range(0, n*n):
            if board[i] == ' ':
                newboard = board[:]
                newboard[i] = 'O'
                var = getcomputermove(newboard, n, depth+1, not(ismax), index, alpha, beta)[0]
                if var > score:
                    score = var
                    index = i
                alpha = max(alpha, score)
                if alpha >= beta:
                    break

    else:
        score = 5
        for i in range(0, n*n):
            if board[i] == ' ':
                newboard = board[:]
                newboard[i] = 'X'
                var = getcomputermove(newboard, n, depth+1, not(ismax), index, alpha, beta)[0]
                if var < score:
                    score = var
                    index = i
                beta = min(beta, score)
                if alpha >= beta:
                    break

    bestmove = [score, index]
    return bestmove

#let's store the board as an array of length n*n
#each element is either X or O or [blank]
n = 3
choice = 'y'

while choice == 'y':
    
    print("\n-----------------------\nWelcome to Tic-Tac-Toe!\n-----------------------")
    board = []
    for i in range(0, n*n):
        board.append(' ')
    printboard(board, n)
    
    while emptyspaces(board, n) == 1:

        validflag = 0
        while validflag == 0:
            move = eval(input("\nEnter your move : "))
            if isvalid(move) == 1:
                validflag = 1
            else:
                print("That's an invalid move, silly. Try again!")
        board[move] = 'X'
        printboard(board, n)

        if checkwin(board, n) == -1:
            print("Wow, you've won!\n")
            break
        elif checkwin(board, n) == 1:
            print("I've beaten you! HA!\n")
            break
        elif checkwin(board, n) == 0:
            print("It's a draw!\n")
            break

        print("\nI'm thinking...")
        chosenmove = getcomputermove(board, n, 0, True, -5, -5, 5)
        move = chosenmove[1]
        board[move] = 'O'
        printboard(board, n)

        if checkwin(board, n) == -1:
            print("Wow, you've won!\n")
            break
        elif checkwin(board, n) == 1:
            print("I've beaten you! HA!\n")
            break
        elif checkwin(board, n) == 0:
            print("It's a draw!\n")
            break
    choice = input("Want another go? (y/n) ")

    if choice == 'y':
        print("\nAll right! Let's see if you can beat me this time.\n")
    else:
        print("\nI see you're not brave enough. See you later!\n")



