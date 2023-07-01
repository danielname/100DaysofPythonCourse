from art import logo
print(logo)
def calculate(n, **kwargs):
    n += kwargs["add"]
    n -= kwargs["subtract"]
    n *= kwargs["multiply"]
    n /= kwargs["divide"]
    return n

def add (*args):
    """Adds two inputs together"""
    sum = 0
    for n in args:
        sum += n
    return sum
def subtract(n1, n2):
    """Subtracts the first input minus the second input"""
    return n1 - n2
def multiply(n1, n2):
    """Multiplies two inputs together"""
    return n1 * n2
def divide(n1, n2):
    """Returns the first inpud divided by the second input"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    starting_number = float(input("What's the first number?\n"))
    running = True
    while running:
        symbol = input("+\n-\n*\n/\nPick an operation\n")
        second_number = float(input("What's the next number?\n"))
        function = operations[symbol]
        result = function(starting_number, second_number)
        print(f"{starting_number} {symbol} {second_number} = {result}")
        starting_number = result
        continue_calcualtion = input(f"Type 'y' to continue calculting with {result}, or type 'n' to start a new calculation.")
        if not continue_calcualtion == "y":
            running = False
            if continue_calcualtion == "n":
                calculator()

calculator()