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
        print("Child tickets are $7.")
else:
        cost += 12
        print("Child tickets are $12.")
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