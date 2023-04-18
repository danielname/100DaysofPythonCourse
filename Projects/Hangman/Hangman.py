# Setup
# Word randomly selected
# Make blanks for each letter in word
# variable with the number of wrong answers till lose defined

# Ask user to guess letter
# if right:
#     letter replaces all blanks where that letter should go
#     letter marked off of bank
#     check if all letters have been guessed
#     if yes:
#         congrats, you win
#     if no:
#         return to line 6
# if wrong:
#     variable -= 1
#     if variable == 0:
#         you lose
#     else:
#         return to line 6


#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
chosen_word.split(" ")
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")