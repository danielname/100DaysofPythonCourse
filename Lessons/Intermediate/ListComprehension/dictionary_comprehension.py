import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddy']

student_scores = {student: random.randint(1, 100) for student in names}

passing_students = {student: score for (student, score) in student_scores.items() if score >= 60}

print(passing_students)

# Exercise 26-4
#You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
#
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word: len(word) for word in sentence.split()}

print(result)
