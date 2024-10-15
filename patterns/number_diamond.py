"""Question:
Write a program to print a number diamond pattern.

Input:An integer n representing the size of the diamond.

Output:Print a number diamond pattern of size n using *.

Example:inserting 5 as input.

output:
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
  1 2 3 4 3 2 1 
    1 2 3 2 1 
      1 2 1 
        1 
"""
#code for the question.

n=int(input())      # taking n as input 
for i in range(1,n+1):
    for x in range(n-i):
        print("  ",end="")
    for t in range(1,i+1):
        print(t,end=" ")
    for k in range(t-1,0,-1):
        print(k,end=" ")
    print()
for w in range(n-1,0,-1):
    for v in range(n-w):
        print("  ",end="")
    for a in range(1,w+1):
        print(a,end=" ")
    for s in range(w-1,0,-1):
        print(s,end=" ")
    print()
