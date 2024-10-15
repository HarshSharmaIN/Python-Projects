''' Question: To Find Prime numbers in range a,b where a and b are two whole numbers.

Input: First Line will contain an integer a representing the start of the range.
Second Line will contain an integer b representing the end of the range.

Output: The List of all Prime numbers between a to b.

For Example:
Input: 5
       13
output: 5 7 11 13

explanation: For the range 5 to 13, the prime numbers are 5, 7, 11, and 13.


Code for the problem using builtin functions:

'''
def find_primes(a, b): #Defining a function
    primes = []
    for num in range(a, b + 1):
        if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num) #Appending the prime numbers into the list
    return primes

a = int(input()) #takes a as input
b = int(input()) #takes b as input
primes = find_primes(a, b)
print("Prime numbers between", a, "and", b, primes) #Prints the output

'''
For Those who are not familiar with Built-in Functions:
Code:
'''
def find_primes(a, b):
    primes = []
    for num in range(a, b + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

a = int(input())
b = int(input())
primes = find_primes(a, b)
print("Prime numbers between", a, "and", b, primes)




