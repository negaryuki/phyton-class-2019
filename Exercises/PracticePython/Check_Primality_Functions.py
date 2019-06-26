# Ask the user for a number and determine whether the number is prime or not.
# Take this opportunity to practice using functions, described below:
# Functions
# Reusable functions
# Default arguments

def get_input():
    return (int(input("Input a Number please :")))


def is_prime(a):
    for i in range(2,a):
        if a % i == 0:
            print(a, "is not Prime")
            break
        else:
            print(a, "is Prime")
            break
    return a

def is_prime2(number):
    prime = True
    for i in range(2,number):
        if number % i == 0:
            prime: False
        return prime


prime_or_not = is_prime(get_input())

print(prime_or_not)
