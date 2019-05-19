# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

print("Ok Let's Start the Rock-Paper-Scissors game " "Player 1, please insert your choice")

player1 = input()
print("ok, now Player 2 what's your choice?")
player2 = input()

player1.lower()
player2.lower()


def compare(p1, p2):
    if p1 == p2:
        return ("It's a tie!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return ("Rock wins!")
        else:
            return ("Paper wins!")
    elif p1 == 'scissors':
        if p2 == 'paper':
            return ("Scissors win!")
        else:
            return ("Rock wins!")
    elif p1 == 'paper':
        if p2 == 'rock':
            return ("Paper wins!")
        else:
            return ("Scissors win!")
    else:
        return ("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()


print(compare(player1, player2))
