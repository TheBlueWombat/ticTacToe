theBoard = {'top-L': 'O', 'top-M': 'X', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'O', 'mid-R': 'X',
            'low-L': 'O', 'low-M': 'X', 'low-R': 'O'}


def ValsList(board):
    tt = []
    inner = []

    for i in range(len(board)):
        inner.append(list(theBoard.values())[i])
        if (i+1) % 3 == 0:
            tt.append(inner)
            inner = []

    print(tt)


ValsList(theBoard)
