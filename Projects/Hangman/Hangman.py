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
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#Step 4
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create Blanks
display = []
for letter in chosen_word:
    display.append('_')

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while display.count("_") > 0 and lives > 0:
    guess = input("Please guess a letter: ").lower()
    if guess in chosen_word:
        # check guessed letter
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                print("Right")
                display[position] = guess
            else:
                print("Wrong")
    else:
        print("Sorry, that letter is not in the word")
        lives -= 1
        print(stages[lives])
    print(f"{' '.join(display)}")
if display.count("_") == 0:
    print("Congratulations! You win!")
else:
    print("Sorry, you lose.")