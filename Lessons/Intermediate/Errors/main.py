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

try:
    file = open("a_file.txt")
    # a_dictionary = {"key": "Value"}
    # value = a_dictionary["not_the_key"]
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else: #this requires no exceptions in try
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    raise KeyError("Got so many keys you think im valet parking")
