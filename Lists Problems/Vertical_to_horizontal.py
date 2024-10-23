'''
Question:
Take input from standard input while you do not get 0 as an input. Print all the inputs separated by space. It is guaranteed that the number of integers are less than 100000.

Input:
The input will contain a series of integers in one line each. Input should be taken while you have not get a 0 as an input.

0 <= input <= 10

Output:
Print the input integers seperated by space.

Sample Input:
6
5
5
0

Sample Output:
6 5 5 0


Code:
'''
inputs = []

while True:
    num = int(input())
    inputs.append(num)
    if num == 0:
        break
        
print(*inputs)