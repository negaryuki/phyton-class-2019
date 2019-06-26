# Ask the user for a number and determine whether the number is prime or not.
# Take this opportunity to practice using functions, described below:
# Functions
# Reusable functions
# Default arguments

def get_input():
    return (int(input("Input a Number please :")))


def is_prime(a):
    for i in range(a):
        if a % i == 0:
            print(a, "is not Prime")
            break
        else:
            print(a, "is Prime")
        return a


num = get_input()
prime_or_not = is_prime(num)

print(prime_or_not)
