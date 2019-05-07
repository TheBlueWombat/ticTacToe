# Tic Tac Toe game!

# the board represented by a dictionary

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def ValsList(board):
    tt = []
    inner = []

    for i in range(len(board)):
        inner.append(list(theBoard.values())[i])
        if (i+1) % 3 == 0:
            tt.append(inner)
            inner = []

    return(tt)

def win_hor(list, turn):
    x, y = 0, 0
    count = 0

    # this for loop checks for a horizontal win. it does check the third row, but it doesn't
    # report for the last line since the loop ends right after it checks the last line
    # and my condition for the win is within the for loop.
    for x in range(len(list)):
        if count == 3:
            print(turn + ' has won horizontally!')
            count = 0 # if there is a win on lines 1 or 2, count would still be set to 3 after the break and i would get the winning message printed twice
            break
        else:
            count = 0
        for y in range(len(list[x])):
            if list[x][y] == turn:
                count += 1
    # this if statement here checks the count to see if the last line is a win
    if count == 3:
        print(turn + ' has won horizontally!')

def win_ver(list, turn):
    x, y = 0, 0
    count = 0

    for y in range(len(list[x])):
        if count == 3:
            print(turn + ' has won vertically!')
            count = 0  # if there is a win on lines 1 or 2, count would still be set to 3 after the break and i would get the winning message printed twice
            break
        else:
            count = 0
        for x in range(len(list)):
            if list[x][y] == turn:
                count += 1
        if count == 3:
            print(turn + ' has won vertically!')

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    if win_hor(ValsList(theBoard), turn):
        print(turn + ' has onw horizontally!')
        break
    if win_ver(ValsList(theBoard), turn):
        print(turn + ' has one vertically!')
        break

printBoard(theBoard)
print()
ValsList(theBoard)
