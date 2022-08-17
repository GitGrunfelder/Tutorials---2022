"""Imports random number generator functions."""
import random

top_of_range = input("I'm thinking of a number from 0 to: ")

if top_of_range.isdigit():

    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Number must be larger than 0.")
        quit("Invalid entry.")
else:
    print("Please type a number above zero.")
    quit("Invalid entry.")

random_number = random.randint(0, top_of_range)

GUESSES = 0

while True:
    GUESSES += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number.")
        continue

    if guess == random_number:
        print("You guessed the random number!!")
        break

    if guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")

if GUESSES == 1:
    print("You guessed the number in", GUESSES, "guess!! You must be psychic!")
else:
    print("You guessed the number in", GUESSES, "guesses! Not bad.")
