import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
comp_choice = random.randint(1,3)
if comp_choice == 1:
    comp_choice = rock
elif comp_choice == 2:
    comp_choice = paper
else:
    comp_choice = scissors
choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
if choice == "0":
    choice = rock
elif choice == "1":
    choice = paper
else:
    choice = scissors

print(f"{choice}\nComputer chose:\n{comp_choice}")
if (choice == rock and comp_choice == paper) or (choice == paper and comp_choice == scissors) or (choice == scissors and comp_choice == rock):
    print("You lose")
elif choice == comp_choice:
    print("It's a draw")
else:
    print("You win")