# The game begins by randomly choosing a word from a predefined list and hiding its characters. The player then guesses letters one at a time, with correct guesses revealing matching characters and incorrect guesses reducing the available attempts. The game ends when the word is fully revealed or all chances are exhausted.

# Create a list of words and randomly select one.
# Initialize variables to store guessed characters and remaining attempts.
# Display the word using underscores for unguessed characters.
# Accept a character from the user.
# Check whether the character exists in the word.
# Continue until the word is guessed or all attempts are exhausted.
# Display the result.

import random

# List of words to choose from 
list_words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
# choosing a string that is random from the sequence above
choosen_string = random.choice(list_words)

guesses = ""
turns = 12

print("\nGuess the characters")

# print(guesses)
# print(choosen_string)

while turns>0:
    # Counter to check for the number of chars have not been displayed
    failed = 0
    for char in choosen_string:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed +=1

    if failed == 0:
        print("You win")
        print("The word is",choosen_string)

    guess = input("Enter a character: ").lower()

    if len(guess) != 1:
        print("Please enter a single character")
        continue

    if guess in guesses:
        print("You already guesses that")
        continue

    guesses += guess

    if guess not in choosen_string:
        turns-=1
        print("Wrong")
        print("You have",turns," guesses")

        if turns == 0:
            print("You loose")
            print("The word was:", choosen_string)
   