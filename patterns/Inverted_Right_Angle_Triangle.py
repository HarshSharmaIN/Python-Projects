'''
Question:
Given an integer n and required to print the following pattern Inverted Right-Angled Triangle.

Input:
First line contains an integer n.

Example:
input = 5
output:
* * * * *
* * * *
* * *
* *
* 


Code:
'''

n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*", end = ' ')
    print()
