from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25
}

caffeinated = False
not_enough_water = lambda: print("Sorry, there is not enough water to make your drink")
not_enough_milk = lambda: print("Sorry, there is not enough milk to make your drink")
not_enough_coffee = lambda: print("Sorry, there is not enough coffee to make your drink")

def pay():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return quarters * COINS['quarter'] + dimes * COINS['dime'] + nickels * COINS['nickel'] + pennies * COINS['penny']

print(logo)
while not caffeinated:
    user_input = input("What kind of coffee would you like? (espresso/latte/cappuccino) ")
    if user_input == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    elif user_input == 'restock':
        resources['water'] += int(input("How much water would you like to add in ml: "))
        resources['milk'] += int(input("How much milk would you like to add in ml: "))
        resources['coffee'] += int(input("How much coffee would you like to add in g: "))

    #     try to make a function that substitutes the name of the coffee for the 3 drinks. If the name is something else, return "Sorry, that drink is not sold by this machine

    elif user_input == 'espresso':
        if MENU['espresso']['ingredients']['water'] > resources['water']:
            not_enough_water()
        if MENU['espresso']['ingredients']['coffee'] > resources['coffee']:
            not_enough_coffee()
        if MENU['espresso']['ingredients']['water'] <= resources['water'] and MENU['espresso']['ingredients']['coffee'] <= resources['coffee']:
            print("Your espresso will cost $1.50, please insert coins:")
            total_pay = pay()
            if total_pay < MENU['espresso']['cost']:
                print("Sorry, that is not enough money. You have been refunded your coins.")
            else:
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                money += MENU['espresso']['cost']
                print(f"Your change is ${round(total_pay - MENU['espresso']['cost'], 2)}\nHere is your espresso ☕. Enjoy!")
    elif user_input == 'latte':
        if MENU['latte']['ingredients']['water'] > resources['water']:
            not_enough_water()
        if MENU['latte']['ingredients']['milk'] > resources['milk']:
            not_enough_milk()
        if MENU['latte']['ingredients']['coffee'] > resources['coffee']:
            not_enough_coffee()
        if MENU['latte']['ingredients']['water'] <= resources['water'] and MENU['latte']['ingredients']['milk'] <= resources['milk'] and MENU['latte']['ingredients']['coffee'] <= resources['coffee']:
            print("Your latte will cost $2.50, please insert coins:")
            total_pay = pay()
            if total_pay < MENU['latte']['cost']:
                print("Sorry, that is not enough money. You have been refunded your coins.")
            else:
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                money += MENU['latte']['cost']
                print(f"Your change is ${round(total_pay - MENU['latte']['cost'], 2)}\nHere is your latte ☕. Enjoy!")
    elif user_input == 'cappuccino':
        if MENU['cappuccino']['ingredients']['water'] > resources['water']:
                not_enough_water()
        if MENU['cappuccino']['ingredients']['milk'] > resources['milk']:
            not_enough_milk()
        if MENU['cappuccino']['ingredients']['coffee'] > resources['coffee']:
            not_enough_coffee()
        if MENU['cappuccino']['ingredients']['water'] <= resources['water'] and MENU['cappuccino']['ingredients']['milk'] <= resources['milk'] and MENU['cappuccino']['ingredients']['coffee'] <= resources['coffee']:
            print("Your cappuccino will cost $3.00, please insert coins:")
            total_pay = pay()
            if total_pay < MENU['cappuccino']['cost']:
                print("Sorry, that is not enough money. You have been refunded your coins.")
            else:
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                money += MENU['cappuccino']['cost']
                print(f"Your change is ${round(total_pay - MENU['cappuccino']['cost'], 2)}\nHere is your cappuccino ☕. Enjoy!")
    happy = input("Would you like another coffee? y/n ").lower()
    if happy == 'n':
        caffeinated = True
