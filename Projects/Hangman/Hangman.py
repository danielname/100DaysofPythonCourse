import random
import Hangman_Words
import Hangman_Art
word_list = Hangman_Words.word_list
chosen_word = random.choice(word_list)
lives = 6
guessed_letters = []
print(Hangman_Art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create Blanks
display = []
for letter in chosen_word:
    display.append('_')
while display.count("_") > 0 and lives > 0:
    guess = input("Please guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You have already guessed the letter {guess}.\nHere is the list of letters that you have used: {guessed_letters}")
        lives -= 1
        print(Hangman_Art.stages[lives])
    else:
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
            print(Hangman_Art.stages[lives])
        print(f"{' '.join(display)}")
        guessed_letters.append(guess)
if display.count("_") == 0:
    print("Congratulations! You win!")
else:
    print("Sorry, you lose.")