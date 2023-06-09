print("hello")
# print is a function because it is called with the parentheses

# in python we define functions with def
def my_function():
    print("hello")
    print("bye")

# calling a function works the same as in JS
my_function()


# functions with inputs
def greet(something = "bill"):
    print(f"Hello {something}")
    print(f"How's it going {something}?")
    print(f"What's up, {something}?")
greet("Joe") #Joe is the argument that gets passed
greet() #if no argument is specified, the predefined "bill" should run.

# multiple parameters
def greet_with(name, location):
    print(f"hello {name}, are you at {location}?")
greet_with("Joe", "home")
# positonal arguments: if no variable is specified, arguments are defined in order

# can call functions with keywords
greet_with(location="away", name="Sam")


# outputs
def my_new_function():
    result = 3 * 2
    return result

def format_name(f_name, l_name):
    return f"{f_name} {l_name}".title()
print(format_name("daniel", "name"))
cap_name = format_name("dAniel", "name")

# multiple returns
# return exits the function, but we can use conditionals to exit where we want
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didnt provide valid inputs"
    return f"{f_name} {l_name}".title()

# Docstrings
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of it"""
    if f_name == "" or l_name == "":
        return "you didnt provide valid inputs"
    return f"{f_name} {l_name}".title()

format_name()


# Exercise 8-1
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#Write your code below this line 👇

def paint_calc(height, width, cover = 5):
    paint_needed = (height * width) / cover
    rounded = round(paint_needed)
    if rounded >= paint_needed:
        print(f"You'll need {rounded} cans of paint.")
    else:
        print(f"You'll need {rounded + 1} cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Exercise 8-2
# You need to write a function that checks whether if the number passed into it is a prime number or not.
#Write your code below this line 👇

def prime_checker(number):
    prime = True
    check_value = 2
    while prime == True and check_value < number:
        if number % check_value == 0:
            prime = False
        else:
            check_value += 1
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


# Exercise 10-1
# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.
#
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] = 29
    return month_days[month - 1]


#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)