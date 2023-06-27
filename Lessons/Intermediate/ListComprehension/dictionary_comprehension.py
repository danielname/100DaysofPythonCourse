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


# Exercise 26-5
#You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

# To convert temp_c into temp_f:
#
# (temp_c * 9/5) + 32 = temp_f
#
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day: (temp * 9 / 5 + 32) for (day, temp) in weather_c.items()}

print(weather_f)


