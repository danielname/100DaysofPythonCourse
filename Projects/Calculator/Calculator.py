import art
print(art.logo)
def add (n1, n2):
    """Adds two inputs together"""
    return n1 + n2
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

starting_number = int(input("What's the first number?\n"))
running = True
symbol = input("+\n-\n*\n/\nPick an operation\n")
second_number = int(input("What's the next number?\n"))
function = operations[symbol]
result = function(starting_number, second_number)
print(f"{starting_number} {symbol} {second_number} = {result}")
continue_calcualtion = input(f"Type 'y' to continue calculting with {result}, or type 'n' to start a new calculation.")