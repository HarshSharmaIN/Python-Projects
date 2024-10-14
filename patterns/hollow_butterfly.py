""" Question:
Write a program to print a hollow butterfly pattern.

Input:
First line will contain an integer n representing the size of the butterfly.

Output:
Print a hollow butterfly pattern of size n using *.

Example:inserting 5 as input

output:
*                 * 
* *             * * 
*   *         *   * 
*     *     *     * 
*       * *       * 
*     *     *     * 
*   *         *   * 
* *             * * 
*                 * 
"""

# Code for the question.

n=int(input())   #take n an integer as input

#applying the condition to print stars and spaces at different palces.

for j in range(1,n+1):
    for i in range(1,2*n+1):
        if i==1 or i==2*n or i==2*n-j+1 or j==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
for m in range (n+1,2*n):
    for k in range(1,2*n+1):
        if k==1 or k==2*n or k==m+1 or k==2*n-m :
            print("* ",end="")
        else:
            print("  ",end='')
    print()
