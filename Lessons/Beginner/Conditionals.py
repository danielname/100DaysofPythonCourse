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
    age = int(input("How old are you? "))
    # nested condition
    cost = 0
    if age < 12:
        cost += 5
        print("Child tickets are $5.")
    elif age <= 18:
        cost += 7
        print("Youth tickets are $7.")
    else:
        if age >= 45 and age <= 55:
            print("Everything is going to be OK. Have a free ride on us!")
        else:
            cost += 12
            print("Adult tickets are $12.")
# multiple if statements
    pic = input("Would you like a picture of your ride for $3? yes/no")
    if pic == "yes":
        cost += 3
    print(f"Your ticket costs ${cost}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Exercise 3-1
# Write a program that works out whether if a given number is an odd or even number.

your_number = int(input("Please type in a number: "))
if your_number % 2 == 0:
    print("Your Number is even!")
else:
    print("Your number is odd!")


# Exercise 3-2
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(float(weight)/float(height)**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# Exercise 3-3
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


# Exercise 3-4
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
# Small Pizza: $15
#
# Medium Pizza: $20
#
# Large Pizza: $25
#
# Pepperoni for Small Pizza: +$2
#
# Pepperoni for Medium or Large Pizza: +$3
#
# Extra cheese for any size pizza: + $1
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cost = 0
if size == "S":
    cost += 15
    if add_pepperoni == "Y":
        cost += 2
    if extra_cheese == "Y":
        cost += 1
elif size == "M":
    cost += 20
    if add_pepperoni == "Y":
        cost += 3
    if extra_cheese == "Y":
        cost += 1
else:
    cost += 25
    if add_pepperoni == "Y":
        cost += 3
    if extra_cheese == "Y":
        cost += 1
print(f"Your final bill is: ${cost}.")


# Exercise 3-5
# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


t_count = (name1 + name2).lower().count("t")
r_count = (name1 + name2).lower().count("r")
u_count = (name1 + name2).lower().count("u")
e_count = (name1 + name2).lower().count("e")
l_count = (name1 + name2).lower().count("l")
o_count = (name1 + name2).lower().count("o")
v_count = (name1 + name2).lower().count("v")
true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count
count = int(str(true_count) + str(love_count))
if count < 10 or count > 90:
    print(f"Your score is {count}, you go together like coke and mentos.")
elif count >= 40 and count <= 50:
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")