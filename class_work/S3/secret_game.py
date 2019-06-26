import random

secret = random.randint(1, 10)
print(secret)
guess = int(input("--->"))
while True:

    if guess < secret:
        print("guess is low")
        guess = int(input("--->"))
    elif guess > secret:
        print("guess is high")
        guess = int(input("--->"))
    else:

        print("you guessed it!")
        break

