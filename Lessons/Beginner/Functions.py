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