import math

def isPrime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
if isPrime(9):
    print("Prime Number")
else:
    print("Non prime number.")
