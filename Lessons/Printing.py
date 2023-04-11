# hello world
print("Hello World")

# concatonation

print("hello" + " " + "Daniel")

# inputs (reused in variables)

# Variables
name = input("what is your name?")
print(name)
name = "John"
print(name)

# Naming
# make your variable names readable so that you will know what they do when you come back to this code over time
# Must Be 1 unite
# Multiple words seperated with underscore NOT camel case
# numbers at the end of a variable
# do not use pre-established names like "new, input, or print"



#Exercise 1-1
#you should run your program and it should print the following:

# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")




# Exercise 1-2
# When you run your program, it should print the following:
#
# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.\ne.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Exercise 1-3
# Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.

name = input("What is your name? ")
length = len(name)
print(length)


# Exercise 1-4
# Write a program that switches the values stored in the variables a and b.

b = input("a: ")
a = input("b: ")
print("a: " + a)
print("b: " + b)

# 1-4 with pre-established code

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

temp = a
a = b
b = temp


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
