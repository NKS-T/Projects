
# Guess the number

from random import randint

guesses = 0
won = 0
play = "y"

while play.lower() != "n":
    number = randint(1, 10)
    guess = int(raw_input("\nGuess a number between 1 and 10 (inclusive): "))

    while guess < 1 or guess > 10:
        print ("ERROR: The number must be between 1 and 10 (inclusive)")
        guess = int(raw_input("Guess a number between 1 and 10: "))

    if guess != number:
        print ("You Lose")
        print ("The correct number was: " + str(number))
    else:
        print ("WINNER!")
        won += 1

    guesses += 1
    play = raw_input("\nPlay again? (Y/N)")

print ("\nYou played " + str(guesses) + " games and won " + str(won))
