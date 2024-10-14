""" Question:
Write a program that takes a positive integer n as input and prints a hollow square pattern of stars with side length n.

Note: There is no need to print space between the stars(*). Please ignore the spaces between the stars (*) in the image and example output.

Input:
First line will contain an integer n representing the size of the square.

Output:
Print a hollow square pattern of stars with side length n

example: inserting 5 as input
 output:
 *****
*   *
*   *
*   *
*****
"""

#Code for the question:

n=int(input())   #take n an integer as input

#applying the condition to print stars and spaces at different palces.
print("*"*n)
for i in range(2,n):
    print("* ",""*(n+1),"*")
print("*"*n)