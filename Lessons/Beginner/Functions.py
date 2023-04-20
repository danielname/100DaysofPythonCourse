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