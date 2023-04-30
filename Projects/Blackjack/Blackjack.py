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
player_cards = [choice(cards), choice(cards)]
player_score = 0
dealer_cards = [choice(cards)]
dealer_score = dealer_cards[0]

for card in player_cards:
    player_score += card
    if player_score > 21 and 11 in player_cards:
        player_score -= 10
        player_cards[player_cards.index(11)] = 1

