
numbers = [1,2,3]
# what are we doing
# for variable item
# in list
new_list = [n + 14 for n in numbers]
print(new_list)

# strings
name = "Daniel"
new_list = [letter for letter in name]
print(new_list)

# on functions that produce lists
my_range = range(1,5)
new_range = [n * 2 for n in my_range]
print(new_range)

# conditional LC
names = ['Alex','Beth','Caroline','Dave','Eleanor', 'Freddie']
short_names = [listname for listname in names if len(listname) <= 4]
print(short_names)
# challenge
long_upper_names = [listname.upper() for listname in names if len(listname) > 4]
print(long_upper_names)

# Exercise 26-1
#You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [n ** 2 for n in numbers]

#Write your code 👆 above:

print(squared_numbers)



# Exercise 26-2
# You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [n for n in numbers if n % 2 == 0]

#Write your code 👆 above:

print(result)

