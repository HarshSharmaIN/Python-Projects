"""Question:Write a program to print a hollow hourglass pattern.

Input:First line will contain an integer n representing the height of the hourglass.

Output:First line will contain an integer n representing the height of the hourglass.

Example: taking 5 as input

output:
* * * * * * * * * 
  *           * 
    *       * 
      *   * 
        * 
      *   * 
    *       * 
  *           * 
* * * * * * * * * """

# code for this question.
n=int(input())   # take n as input
for i in range(1,2*n):
    for j in range(1,2*n):
        if i==1 or i==j or j==(2*n-i) or i==(2*n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
