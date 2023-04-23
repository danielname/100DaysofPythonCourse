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

# Exercise 9-1
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
#
# DO NOT modify lines 1-7 to change the existing student_scores dictionary.
#
# DO NOT write any print statements.
#
# This is the scoring criteria:
#
# Scores 91 - 100: Grade = "Outstanding"
#
# Scores 81 - 90: Grade = "Exceeds Expectations"
#
# Scores 71 - 80: Grade = "Acceptable"
#
# Scores 70 or lower: Grade = "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    elif student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] <= 100:
        student_grades[student] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)