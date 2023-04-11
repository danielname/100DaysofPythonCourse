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