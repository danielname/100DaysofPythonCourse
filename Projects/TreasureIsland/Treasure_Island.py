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
print('It is a nice day! When you wake up, you get the mail and receive a letter from your weird, pirate uncle, \nwho claims there is a lost treasure on a deserted island near your home.')

game = True
lives = 2

first_step = input('To take up the challenge of finding the treasure, type "adventure." To stay home and play video games type "stay."\n')
if first_step.lower() == "adventure" or first_step.lower() == "adventure.":
    while game:
        direction = input('\nYou\'re at a cross road. You feel a salty breeze coming from the left, dry warmth coming from the right.\nWhere do you want to go? Type "left" or "right"\n')
        if direction.lower() == "left":
            while game:
                lake = input('\nYou came to a lake. You don\'t see anything unusual, but the water is a bit choppy. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.\n')
                if lake.lower() == "wait":
                    while game:
                        shore = input('\nYou arrive at the island unharmed. As you step off the boat you notice a beach full of crabs and gulls, a forest with tightly paced trees, and a mountain.\nType "shore" to check the beach, "forest" to check the forest, or "cliff" to climb up the mountain.\n')
                        if shore.lower() == "forest":
                            while game:
                                house = input("\nThrough the trees, there is a house with 3 glazed glass doors: one shines red, one yellow, and one blue. Which color door do you choose to go through?\n")
                                if house.lower() == "yellow":
                                    while game:
                                        gold = input('\nThe door leads to an empty shed with white walls, no cieling, and only the earth below as a floor. Before you leave, you see a golden coin on the floor.\nYou wonder if this is a trap or a sign of the treasure. Type "dig" to dig for gold or "leave" to try to escape to safety.\n')
                                        if gold.lower() == "dig":
                                            print("You found an amazing treasure! Congratulations, you win!")
                                            game = False
                                        else:
                                            print("At the end of the day you are still a coward. You should have stayed home and played video games. Game Over.")
                                            game = False
                                elif house.lower() == "blue":
                                    print("You released wild beasts! They only want freedom, but attack you on the way out. You try to play dead until they leave.")
                                    lives -= 1
                                    if lives == 0:
                                        game = False
                                else:
                                    print("You were trapped in the house, which caught ablaze! You perish in the fire! GAME OVER!")
                                    game = False
                        elif shore.lower() == "cliff":
                            print("As you start to climb, the skies darken and it begins to rain. you slip and land at the base, flat on your back. It's hard to breathe, but you'll do your best to make it back to the dock.")
                            lives -= 1
                            if lives == 0:
                                game = False
                        else:
                            print("The shoreline is beautiful, but there isn't anything of value here. As you start to walk back to the dock, you are pinched in the toes by the crabs.")
                            lives -= 1
                            if lives == 0:
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
