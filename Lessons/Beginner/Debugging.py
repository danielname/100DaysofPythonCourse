############DEBUGGING#####################

# # Describe Problem
# the function never prints "You got it"
# because the range function does not include the upper limit.

# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# fix
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()


# # Reproduce the Bug
# error happens when dice_num is 6. If I print dice_imgs[6], it always errors

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# fix
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer
# 1994 is not taken into account as either millenial or gen Z. one of the conditions needs a <= or >=

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# # Fix the Errors
# age is a string, need to int()
# need to indent print()
# need an f string to print the value of age

# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# Fix
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")


# #Print is Your Friend
# redefinition is unnecessary
# == on word_per_page input doesnt work

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Fix
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# #Use a Debugger
# adding items outside of loop

# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])

# Fix
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])


# Exercise 13-1
# if has =, which is an assigner, needs == to test equality
# number = int(input("Which number do you want to check?"))
#
# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# Exercise 13-2
# year is currently a string, needs to be an int

# year = input("Which year do you want to check?")
#
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")


# Fix
year = int(input("Which year do you want to check?"))

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
