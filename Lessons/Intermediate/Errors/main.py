# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "Value"}
# value = a_dictionary["not_the_key"]

# IndexError
# fruit_list = ["apple", "pear", "cherry"]
# fruit = fruit_list[3]

# type error
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     # a_dictionary = {"key": "Value"}
#     # value = a_dictionary["not_the_key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else: #this requires no exceptions in try
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise KeyError("Got so many keys you think im valet parking")

# height = float(input("height: "))
# weight = int(input("weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be above 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)


# Exercise 30-1
# Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie". e.g.

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(0)


# Exercise 30-2
# Use what you've learnt about exception handling to prevent the program from crashing.

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        print("No Likes on post")

print(total_likes)
