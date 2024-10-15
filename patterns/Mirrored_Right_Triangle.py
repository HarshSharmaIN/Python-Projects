'''
Question: Write a Python program that takes a positive integer input n and prints a mirrored right-angled triangle pattern of stars (*).
The triangle should have n rows, with the stars aligned to the right side.

Input: First line contains an integer n, which represents the number of rows of stars in mirrored right angled triangle pattern.

Output: Print a mirrored right angled triangle star pattern of n rows.

For Example:
Input: 5
 
Output: 
    *
   **
  ***
 ****
*****

The Code is as Follows:

'''

n = int(input()) #Input Taken
s = n-1 
for i in range(1):
    for j in range(1,n+1):
        print(s*" " + j*"*") #It Prints Spaces Followed By stars
        s -= 1

#The code prints a right-aligned triangle of asterisks with n rows. It decreases the number of leading spaces (s) while increasing the number of asterisks (j) in each row.