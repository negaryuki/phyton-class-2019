# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# Extras:

# Keep the game going until the user types “exit”

# Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

correct_answer = random.randint(1, 9)
count = 0

print("welcome to the Guessing game! \(^o^)/")
player_guess = int(input("please enter your guess:"))

while True:

    if player_guess < correct_answer:
        print("guess is low (~_~)!")
        player_guess = int(input("Try again:"))
        count +=1
    elif player_guess > correct_answer:
        print("guess is high (X_X)")
        player_guess = int(input("Try again:"))
        count += 1
    else:

        print("you guessed it! (*v*)/~")
        count += 1
        break

print("it took you", count, "tries!")