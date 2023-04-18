# Lists
fruits = ["apple", "pear", "cherry"]
print(fruits[1])
print(fruits[-1])
fruits[0] = "lettuce"
print(fruits[0])
fruits.append("orange")
print(fruits)
fruits.extend(["melon", "raspberry"])
print(fruits)

# nested lists
pest_fruit = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
pest_veg = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen =[pest_fruit, pest_veg]
print(dirty_dozen)
print(dirty_dozen[0][3])


# Exercise 4-2
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
buyer = names[int(random.random() * len(names))]
print(f"{buyer} is going to buy the meal today!")

# Exercise 4-3
# You are going to write a program that will mark a spot with an X.
#
# In the starting code, you will find a variable called map.
#
# This map contains a nested list. When map is printed this is what the nested list looks like:
#
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
#
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line.
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# Now it looks a bit more like the coordinates of a real map:
# Your job is to write a program that allows you to mark a square on the map using a two-digit system.
#
# The first digit in the input will specify the column (the position on the horizontal axis).
#
# The second digit in the input will specify the row number (the position on the vertical axis).

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

position.split(" ")
map[int(position[1]) - 1][int(position[0]) - 1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
