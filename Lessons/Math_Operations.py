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


# Exercise 2-1
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