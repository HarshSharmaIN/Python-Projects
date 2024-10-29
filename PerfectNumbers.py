'''
Question:-
 Perfect Numbers in range


Given two integers a and b, write a program to find and print all perfect numbers in the range from a to b.
A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).

Note:-
This is a functional problem. You do not need to take any input. You just need to complete the function, and print the output.
Input
First Line will contain an integer a representing the start of the range.
Second Line will contain an integer b representing the end of the range.
Output
Print all perfect numbers between a and b in a space-separated matter.
Example
Input
1
100

Output
6 28
 '''

 #Answer
 def print_perfect_numbers(a, b):
    for i in range(a, b + 1):
        count = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                count += j
        if count == i:
            print(i, end=" ")