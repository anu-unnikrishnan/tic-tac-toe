#play Tic-Tac-Toe with one human player, one computer player using AI
#use minimax algorithm for AI decision-making
#use alpha-beta pruning to make minimax more efficient

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

#check if move is valid i.e. on the board and blank
def isvalid(move):
    if move >= 0 and move < n*n:
        if board[move] == ' ':
            return 1
    return 0

#return score and index for best move
def getcomputermove(board, n, depth, ismax, index, alpha, beta):
    
    #if we have reached a terminal state (win/lose/draw)
    if checkwin(board, n) == +1 or checkwin(board, n) == -1 or checkwin(board, n) == 0:
        score = checkwin(board, n)
        bestmove = [score, index]
        return bestmove
    
    #if it's the maximiser's turn
    if ismax == True:
        score = -5
        #loop through to find blank spaces
        for i in range(0, n*n):
            if board[i] == ' ':
                newboard = board[:] #making a copy of the board
                newboard[i] = 'O'
                #maximiser calls the minimiser
                var = getcomputermove(newboard, n, depth+1, not(ismax), index, alpha, beta)[0]
                #if there's a better maximum score, choose that
                if var > score:
                    score = var
                    index = i
                #if there's a better alpha, choose that
                alpha = max(alpha, score)
                #check if we can prune (will that path give a better option?)
                if alpha >= beta:
                    break

    #if it's the minimiser's turn
    else:
        score = 5
        #loop through to find blank spaces
        for i in range(0, n*n):
            if board[i] == ' ':
                newboard = board[:] #making a copy of the board
                newboard[i] = 'X'
                #minimiser calls the maximiser
                var = getcomputermove(newboard, n, depth+1, not(ismax), index, alpha, beta)[0]
                #if there's a better minimum score, choose that
                if var < score:
                    score = var
                    index = i
                #if there's a better beta, choose that
                beta = min(beta, score)
                #check if we can prune (will that path give a better option?)
                if alpha >= beta:
                    break

    bestmove = [score, index]
    return bestmove

#let's store the board as an array of length n*n
#each element is either X or O or [blank]
n = 3
choice = 'y'

#play as many games as the player wants
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
        #keep going until the player enters a valid move
        while validflag == 0:
            move = eval(input("\nEnter your move : "))
            if isvalid(move) == 1:
                validflag = 1
            else:
                print("That's an invalid move, silly. Try again!")
        #play X there
        board[move] = 'X'
        printboard(board, n)

        #check if anyone has won yet
        if checkwin(board, n) == -1:
            print("Wow, you've won!\n")
            break
        elif checkwin(board, n) == 1:
            print("I've beaten you! HA!\n")
            break
        elif checkwin(board, n) == 0:
            print("It's a draw!\n")
            break

        #computer calculates the best move based on minimax
        print("\nI'm thinking...")
        chosenmove = getcomputermove(board, n, 0, True, -5, -5, 5) #depth = 0, ismax = True, index = -5, alpha = -5, beta = +5
        move = chosenmove[1] #chosenmove = [score, index] of best move
        #play O there
        board[move] = 'O'
        printboard(board, n)

        #check if anyone has won yet
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



