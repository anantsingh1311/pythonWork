"""Creating a number guessing game"""

import random

# Introduction

print("Welcome to the Number guessing game, I am your host tonight! \n")
print("Enter your name below: \n")
name = input("Name:")
print(f"\nWelcome {name}")

# Asking the user for Upper and lower bound values they want to play for:
print("Please enter the upper bound and lower bound value you would Like to play with:\n")
lower_Bound = int(input("Lower Bound Value:"))
upper_Bound = int(input("Upper Bound Value:"))
print(f"Lets start the game with Lower bound Value of {lower_Bound} and an upper bound value of {upper_Bound}")

# Number of guesses the user gets is 3:
guesses = 0
# setting up an answer which is a random int
answer = random.randint(lower_Bound,upper_Bound)
print(answer)
while guesses<3:
    print("Enter your guess:")
    number = int(input("Guess:"))
    if (number > answer):
        print("Your answer is too high try again")
    elif (number < answer):
        print("Too Low,try again")
    elif (number == answer):
        print("You win")
        print(f"Congrats {name}")
        break
    guesses +=1
else:
    print(f"You Loose, the answer was:{answer}")
