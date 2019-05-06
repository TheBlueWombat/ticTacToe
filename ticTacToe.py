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


def checkWinner(board):
    ttVals = []
    ttFinal = []
    inner = []

    for v in board.values():
        ttVals.append(v)

    for i in range(len(ttVals)):
        inner.append(ttVals[i])
        if (i+1) % 3 == 0:
            ttFinal.append(inner)
            inner = []

    print(ttFinal)


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

printBoard(theBoard)
checkWinner(theBoard)
