'''
Player1's symbol is "X" 
Player2's symbol is "O"

The player's should give a input which is any one number which is available in the grid . 
so that at the position at which that number exists will be updated with the player's symbol.
'''




board = [
         ['0','1','2'],
         ['3','4','5'],
         ['6','7','8']
        ]

def print_board():
  for i in board:
    print(i)


def p1():

  n = int(input("Player1's_move.  "))
  row = n//3 
  column = n%3
  board[row][column]="X"
  print_board()

def p2():

  n = int(input("Player2's_move.  "))
  row = n//3
  column = n%3
  board[row][column]="O"
  print_board()

def end():
  if board[0][0]==board[1][0]==board[2][0]:
    return(board[0][0])

  elif board[0][1]==board[1][1]==board[2][1]:
    return(board[0][1])

  elif board[0][2]==board[1][2]==board[2][2]:
    return(board[0][2])


  elif board[0][0]==board[0][1]==board[0][2]:
    return(board[0][0])

  elif board[1][0]==board[1][1]==board[1][2]:
    return(board[1][1])

  elif board[2][0]==board[2][1]==board[2][2]:
    return(board[2][0])


  elif board[0][0]==board[1][1]==board[2][2]:
    return(board[0][0])

  elif board[0][2]==board[1][1]==board[2][0]:
    return(board[0][2])

  else:
    return("draw")




print_board()
count=0
for i in range(5):
  p1()
  count+=1
  a = end()
  if a=="X":
    print("Game Ended")
    print("Player1 won")
    break
  if count==9:
    print("draw")
    break

  p2()
  count+=1
  a = end()
  if a=="O":
    print("Game Ended")
    print("Player2 won")
    break