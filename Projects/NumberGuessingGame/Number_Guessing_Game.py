#Number Guessing Game Objectives:
from random import randint
number = randint(1,100)
# Include an ASCII art logo.
from art import logo
print(logo)

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPlease pick a difficulty level: type 'easy' or 'hard'.\n").lower()
if difficulty == "easy":
    turns = 10
else:
    turns = 5

# Allow the player to submit a guess for a number between 1 and 100.
game = True
while game and turns > 0:
    guess = int(input("Please guess my number.\n"))
    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    if guess > number:
        print(f"Your guess was too high! {turns - 1} guesses remain.")
        turns -= 1
    elif guess < number:
        print(f"Your guess was too Low! {turns - 1} guesses remain.")
        turns -= 1
    else:
        print(f"That is correct! {guess} is the number!")
        game = False
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
if turns == 0:
    print(f"You ran out of turns; you lose. The number was {number}")
