'''
Question: given an integer n and Required to print the pattern of a Right-Angled Triangle.

Input: First line contains an integer n

Example:
Input = 5
Output:
*
* *
* * *
* * * *
* * * * * 

The Code is as Follows:
'''

n = int(input()) #input from user
for i in range(1):
    for j in range(1,n+1):
        print('* '*j) #prints * in form of right angled triangle

"""The Following Code Iterates in range of the input to produce the desired right angled triangle"""