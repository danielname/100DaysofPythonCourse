# for loop
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# range function
for number in range(1,11,2):
    print(number)


# While Loop
# while condition == true:
#     what is repeated

# when to use while vs for
# use for when you have to do something with each item in a list
# use for to control exactly how many times you do something with range
# while is better for a general condition, but be careful that the condition must be able to be false

# Exercise 5-1
# You are going to write a program that calculates the average student height from a List of heights.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
for number in student_heights:
    sum += number
print(round(sum / len(student_heights)))

# Exercise 5-2
# You are going to write a program that calculates the highest score from a List of scores.
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
high_score = 0
for value in student_scores:
    if value > high_score:
        high_score = value
print(f"The highest score in the class is: {high_score}")

# Exercise 5-3
sum = 0
for number in range(0,101,2):
    sum += number
print(sum)

# Exercise 5-4
# fizzbuzz
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)