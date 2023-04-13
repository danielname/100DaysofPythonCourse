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
print("Your mission is to find the treasure.")

#Write your code below this line 👇
direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')
if direction.lower() == "left":
    lake = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if lake.lower() == "wait":
        house = input("You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which color door do you choose to go through?\n")
        if house.lower() == "yellow":
            print("You found a fantastic treasure! Congratulations, you win!")
        elif house.lower() == "blue":
            print("You released wild beasts that tore you to sheds and ate your corpse. GAME OVER!")
        else:
            print("You were trapped in the house, which caught ablaze! You perish in the fire! GAME OVER!")
    else:
        print("You were attacked by a trout and died. GAME OVER!")
else:
    print("You fell in a hole and died. GAME OVER!")