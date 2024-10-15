'''
Question: 
Given an integer n and required to print the pattern Square of Stars.

Input:
An Integer n

Example:
Input: 5
Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

Code:
'''
n = int(input())
for i in range(n):
    for j in range(1,n+1):
        print('*', end =' ')
    print('')
