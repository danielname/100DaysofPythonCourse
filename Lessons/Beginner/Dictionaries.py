#similar to hash tables, we have a key value pair where we have a word and an associated definition
programming_dictionary = {
    "bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["bug"])

# make sure the key is in the correct data type and spelled correctly
number_dictionary = {
    1: "hello world",
    2: "goodbye world"
}
print(number_dictionary[1])

# adding an item to a dictionary
programming_dictionary["loop"] = "The action of doing something over and over again"
print(programming_dictionary)
# programming_dictionary = {}
# print(programming_dictionary)

programming_dictionary["bug"] = "A moth in your computer"
print(programming_dictionary["bug"])

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])