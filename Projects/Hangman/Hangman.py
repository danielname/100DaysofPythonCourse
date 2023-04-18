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
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display.append('_')
guess = input("Please guess a letter: ").lower()


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        print("Right")
        display[position] = guess
    else:
        print("Wrong")

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)