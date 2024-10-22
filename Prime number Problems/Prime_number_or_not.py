'''
Question: Check if a number is prime or not

Input: Take an integer as input 

Output: If The number is prime, Then print "is a prime number"
Else, "is not a prime number"


Example:
Input: 5
Output: is a prime number

Code:
'''

def is_prime(number): #defining a function
    if number < 2: # No number is prime if its less than 2
        return False
    elif number==2: # Since 2 is the only prime number we have to check for it before
        return True
    else:
        for i in range(2, int(number**0.5) + 1): #The code checks the range between 1,square root of the number.
            if number % i == 0: 
                return False
        return True
    

# Input from the user
num = int(input("Enter a number: "))

# Checking if the number is prime
if is_prime(num):
    print(num, "Is a prime number.")
else:
    print(num, "Is not a prime number.")
