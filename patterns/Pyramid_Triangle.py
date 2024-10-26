'''
Question:
Given an integer n, print the following pattern in the form of a centered pyramid.

Input:
The first line contains an integer n.

Example:
input = 5
output:
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 

Code:
'''

n = int(input("Enter the number of rows: "))
for i in range(n):
    # Print spaces for alignment
    print(" " * (n - i - 1), end="")
    # Print stars with a space in between
    print("* " * (i + 1))
