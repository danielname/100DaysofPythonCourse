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

# Exercise
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
buyer = names[int(random.random() * len(names))]
print(f"{buyer} is going to buy the meal today!")