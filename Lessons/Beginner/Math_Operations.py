# additon
3+2
# SUBTRACTION
3-2
# multiplication
3*2
# division (returns a float)
3/2
# exponentiation
3**2

print(3*(3+3)/3-3)

# Number manipulation
# two methods for floor
print(int(47/13))
print(47//13)

# rounding
print(round(47/13, 2))

# iteration
stored_number = 15 / 3
stored_number/= 3
print(round(stored_number))

# F strings
# bad
score = 0
height = 1.8
is_winning = True

print("Your score is: " + str(score) + " and it is " + str(is_winning) + " that you are winning! While I have you on the line, your height in meters is: " + str(height))

# good
print(f"Your score is: {score} and it is {is_winning} that you are winning! While I have you on the line, your height is {height} meters tall.")


# Exercise 2-2
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(float(weight)/float(height)**2)



# Exercise 2-3
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x days, y weeks, and z months left.
#
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
