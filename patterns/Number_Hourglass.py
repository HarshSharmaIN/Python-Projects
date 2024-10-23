'''
Question: You are given an integer n and you need to print the following pattern of height 2n-1.
There is atleast-one space between any two numbers in the same line. Or in other words, space exists between two numbers.



Input:
The first line contains an integer n.

Output:
Print the required pattern.
(Include space between the numbers )

Code is as follows:
'''
n=int(input()) #Input
for i in range(1,n+1):
    for j in range(1,i):
        print("",end=" ")
    for k in range(i,n+1):
        print(k,end=" ")
        for m in range(0):
            print(" ",end="")
    print()
    
for i in range(n-1,0,-1):
    for j in range(1,i):
        print("",end=" ")
    for k in range(i,n+1):
        print(k,sep=" ",end=" ")
        for m in range(0):
            print(" ",end="")
    print()
