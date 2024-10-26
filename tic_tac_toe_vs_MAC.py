''' 
It is a tic tac toe game.
It is a player vs computer game.

Here in this game , YOU (player) should do the first move .
And your symbol is "X". whereas computer's symbol is "O".

The player's should give a input which is any one number which is available in the grid . 
so that at the position at which that number exists will be updated with the player's symbol.

'''
import random

board = [
         ['0','1','2'],
         ['3','4','5'],
         ['6','7','8']
        ]

def print_board():
  for i in board:
    print(i)


def p1():
  n = int(input(namex))
  row = n//3
  column = n%3
  board[row][column]="X"
  print_board()
  print()
  global arr
  arr.remove(n)



def mac():
  global arr
  n = random.choice(arr)
  print("Mac's move is","   ",n)
  row = n//3
  column = n%3
  board[row][column]="O"
  print_board()
  print()
  arr.remove(n)


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




arr = [0,1,2,3,4,5,6,7,8]
count=0

name = input("Your sweet name please   ")
print()
namex = name+"'s move.    "

print_board()
print()

for i in range(5):
  p1()
  count+=1
  a = end()
  if a=="X":
    print("Game Ended")
    print(name,"won")
    break
  if count==9:
    print("Game Drawn")
    break

  mac()
  count+=1
  a = end()
  if a=="O":
    print("Game Ended")
    print("Mac won")
    break