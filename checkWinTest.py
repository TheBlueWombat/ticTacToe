theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'O', 'mid-R': 'O',
            'low-L': 'O', 'low-M': 'X', 'low-R': 'X'}


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
    won = False

    # this for loop checks for a horizontal win. it does check the third row, but it doesn't
    # report for the last line since the loop ends right after it checks the last line
    # and my condition for the win is within the for loop.
    for x in range(len(list)):
        if count == 3:
            won = True
            count = 0 # if there is a win on lines 1 or 2, count would still be set to 3 after the break and i would get the winning message printed twice
            break
        else:
            count = 0
        for y in range(len(list[x])):
            if list[x][y] == turn:
                count += 1
    # this if statement here checks the count to see if the last line is a win
    if count == 3:
        won = True

def win_ver(list, turn):
    x, y = 0, 0
    count = 0
    won = False

    for y in range(len(list[x])):
        if count == 3:
            won = True
            count = 0  # if there is a win on lines 1 or 2, count would still be set to 3 after the break and i would get the winning message printed twice
            break
        else:
            count = 0
        for x in range(len(list)):
            if list[x][y] == turn:
                count += 1
        if count == 3:
            won = True



print(ValsList(theBoard))
win_hor(ValsList(theBoard), 'O')
win_ver(ValsList(theBoard), 'O')
