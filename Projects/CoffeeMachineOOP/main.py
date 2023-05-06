from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
pot = CoffeeMaker()
money = MoneyMachine()

order = input(f"What would you like to drink? {menu.get_items()}").lower()
if order == "report":
    pot.report()
    money.report()
else:
    drink = menu.find_drink(order)
    if pot.is_resource_sufficient(drink):
        if money.make_payment(drink.cost):
            pot.make_coffee(drink)
