print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print('It is a nice day! When you wake up, you get the mail and receive a letter from your weird, pirate uncle, who claims there is a lost treasure on a deserted island near your home.')

game = True
lives = 2

first_step = input('To take up the challenge of finding the treasure, type "adventure." To stay home and play video games type "stay."')
if first_step.lower() == "adventure" or first_step.lower() == "adventure.":
    while game:
        direction = input('You\'re at a cross road. You feel a salty breeze coming from the left, dry warmth coming from the right. Where do you want to go? Type "left" or "right"\n')
        if direction.lower() == "left":
            while game:
                lake = input('You came to a lake. You don\'t see anything unusual, but the water is a bit choppy. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
                if lake.lower() == "wait":
                    while game:
                        house = input("You arrive at the island unharmed. There is a house with 3 glazed glass doors: one shines red, one yellow, and one blue. Which color door do you choose to go through?\n")
                        if house.lower() == "yellow":
                            print("You found a fantastic treasure! Congratulations, you win!")
                            game = False
                        elif house.lower() == "blue":
                            print("You released wild beasts that tore you to shreds and ate your corpse. GAME OVER!")
                            game = False
                        else:
                            print("You were trapped in the house, which caught ablaze! You perish in the fire! GAME OVER!")
                            game = False
                else:
                    print("You were attacked by a trout. As scared as you are, you try to swim back to land.")
                    lives -= 1
                    if lives == 0:
                        game = False
        else:
            print("You find yourself in a desert. You fell in a hole and twisted your ankle. It hurts, but you're going to try to get back to the cross road.")
            lives -= 1
            if lives == 0:
                game = False
else:
    print("You stay and live an uneventful life. You die sad and alone. GAME OVER!")

if lives < 1:
    print("You died, GAME OVER!")
