"""Import random functions"""
import random

USER_WINS = 0
COMPUTER_WINS = 0
TIES = 0
choicesList = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()

    if user_input == "q":
        break #ends program
    if user_input not in choicesList:
        continue #restarts while-loop from beginning.
    result = random.choice(choicesList) #picks a winning choice
    computer_pick = random.choice(choicesList) #computer randomly chooses their guess.
    if user_input == result and computer_pick == result: #if both guess right, tie counter increases
        TIES += 1
        print("Result was", result,". Both you and computer guessed correctly, it is a tie!")
    elif user_input != result and computer_pick != result:
        print("Result was", result,". Neither party guessed correctly.")
    elif user_input == result and computer_pick != result:
        USER_WINS += 1
        print("Result was", result,". User wins!")
    else:
        COMPUTER_WINS += 1
        print("Result was", result,". Computer wins!")


#Outside of while loop - print final score, say goodbye.
print("Thanks for playing.")
print("The final score was computer:", COMPUTER_WINS)
print("User:", USER_WINS)
print("Ties:", TIES)
print("Goodbye")
