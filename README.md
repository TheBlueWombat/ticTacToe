# ticTacToe
Python Project: tic tac toe game


```
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
 ```
    
  This was my first function (incomplete). My idea is to take the values in the dictionary, 
  as the players place their X's and O's and convert those values into a list that I can
  iterate through. Once in list form, I will compare the values in some way and look for
  one of the 8 possible winning patterns.
 
 I further improved this function and reduced the amount of lists and for loops:
 
 ```
 def ValsList(board):
    tt = []
    inner = []

    for i in range(len(board)):
        inner.append(list(theBoard.values())[i])
        if (i+1) % 3 == 0:
            tt.append(inner)
            inner = []
  ```
 
 I was wondering if i can reduce it even further and use only the tt list but I think it would 
 be too complicated right now. first I want to make sure I can get this to work and then
 I will worry about making it pretty.
 
 
