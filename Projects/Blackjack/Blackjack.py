from art import logo
from random import choice
print(logo)

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

#Difficulty Super Expert ☠️: Don't use any hints to complete the project. <-this is my choice

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []

def new_game():

    def deal_card(player):
        player.append(choice(cards))

    def count_score(player):
        sum = 0
        for card in player:
            sum += card
            if sum > 21 and 11 in player:
                sum -= 10
                player[player.index(11)] = 1
        return sum

    for card in range(0,2):
        deal_card(player)
        count_score(player)
    deal_card(dealer)

    game = True

    while game:
        print(f"    Your cards: {player}, current score: {count_score(player)}\n    Computer's first card: {dealer[0]}")
        hit = input("Type 'y' to hit, type 'n' to stay").lower()
        if hit == "y":
            deal_card(player)
            score = count_score(player)
            if score > 21:
                game = False
                print(f"    Your cards: {player}, current score: {score}\nBust! You lose!")
        else:
            game = False

    if count_score(player) <= 21:
        while count_score(dealer) < 17:
            deal_card(dealer)
            score = count_score(dealer)
            print(f"    Computer's cards: {dealer}, score: {score}")
            if score > 21:
                print("Computer busts! You win!")

    if count_score(player) <= 21 and count_score(dealer) <= 21:
        player_score = count_score(player)
        dealer_score = count_score(dealer)
        if player_score > dealer_score:
            print("You win!")
        elif dealer_score > player_score:
            print("You Lose")
        else:
            print("Push")

new_game()