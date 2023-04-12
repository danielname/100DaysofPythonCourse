# control flow
# if condition:
#     do this
# else:
#     do this

water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Exercise 3-1
# Write a program that works out whether if a given number is an odd or even number.

your_number = int(input("Please type in a number: "))
if your_number % 2 == 0:
    print("Your Number is even!")
else:
    print("Your number is odd!")