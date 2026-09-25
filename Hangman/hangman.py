# importing packages:

import random

# words to choose from
words = ["apple","banana","grapes","peach"]

# chosen word
chose_word = random.choice(words)

# print(chose_word)


hang_man = [
"""
----------
|        |
         |
         |
         |
==========
"""
,

"""
----------
|        |
O        |
         |
         |
==========
"""
,
"""
----------
|        |
O        |
|        |
         |
==========
"""

,

"""
----------
 |        |
 O        |
/|\\      |
          |
==========
"""

,
"""
----------
 |        |
 O        |
/|\\      |
  \\      |
==========
"""
,
"""
----------
 |        |
 O        |
/|\\      |
/ \\      |
==========
"""
]
guessed = ""
# to keep a track of number of guesses left
wrong_guesses = 0
# to keep a track of max attempts left
max_attempts = len(hang_man)-1

# Ask for user details:

# print("\nPlease enter your name: \n")

# name = input("Name: ")

# print(f"Welcome {name} to hangman")

while(wrong_guesses < max_attempts):

    display = ""

    for char in chose_word:
        if char in guessed:
            display += char
        else:
            display += "_"
            # wrong_guesses +=1
            # print(hang_man[wrong_guesses])

    print(display)

       
    if "_" not in display:
             print("You win")
             break

    print("\nEnter a word you are trying to guess\n")
    guess = input("Word: ")


    if(len(guess) != 1):
        print("Enter a character not a full word")
        continue

    if guess in guessed:
        print("You already guessed that.")
        continue

    if guess not in chose_word:
            wrong_guesses += 1
            print(hang_man[wrong_guesses])
    else :
            print("Correct guess")

    guessed += guess

    # Now I have to iterate over every character in the chosen word to see if the guess taken matches 
    # any character in the word and if it does, I replace it with the guessed char
    # if not I cancel out an attempt and increments wrong guess




    