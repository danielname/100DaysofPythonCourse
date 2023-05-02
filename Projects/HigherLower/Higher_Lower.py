from game_data import data
import art
from random import randint

game = True
first_person = data[randint(0, len(data) - 1)]
def select_next():
    pick = data[randint(0, len(data) - 1)]
    while pick == first_person:
        pick = data[randint(0, len(data) - 1)]
    return pick
second_person = select_next()
points = 0

print(art.logo)

while game:
    if first_person['follower_count'] > second_person['follower_count']:
        winner = 'a'
    else:
        winner = 'b'

    print(f"Compare A: {first_person['name']}, a(n) {first_person['description']}, from {first_person['country']}.\n{art.vs}\nAgainst B: {second_person['name']}, a(n) {second_person['description']}, from {second_person['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B'\n").lower()

    if guess == winner:
        points += 1
        print("Correct!")
        first_person = second_person
        second_person = select_next()
    else:
        game = False
        print(f"Sorry, {first_person['name']} has {first_person['follower_count']} followers and {second_person['name']} has {second_person['follower_count']}. You lose!\nFinal score: {points}")
