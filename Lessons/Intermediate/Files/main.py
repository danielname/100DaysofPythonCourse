# Accessing a file (basic)
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Using with to open files (saves needing to close file)
try:
    with open("my_file.txt") as file:
        contents = file.read()
        print(contents)
except:


# Writing to a file (deletes the previous content)
    with open("my_file.txt", mode="w") as file:
        file.write("Adding some new text")

# appending to a file with mode="a"
with open("my_file.txt", mode="a") as file:
    file.write("\ndfghblakshnbfgkadsAdding some new text")

    # If you try to open a file in write mode that doesnt exist, then python will create that file from scratch
with open("big_loser.txt", mode="w") as file:
    file.write("I feel like a winner")
