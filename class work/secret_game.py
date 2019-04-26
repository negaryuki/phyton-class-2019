import random

secret = random.randint(1, 10)
guess = int(input())

while secret != "guess":
    print
    if guess < secret:
        print("guess is low")
        guess = int(input())
    elif guess > secret:
        print("guess is high")
        guess = int(input())
    else:
        print
        print("you guessed it!")
        break

