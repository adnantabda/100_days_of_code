"""Coffee Machine Code - OOP.
Project for Angela Wu's 100 days of code challenges.
"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

active = True
while active:
    list_menu = menu.get_items()        # Get available items
    print(f"What would you like to have? \n\t- {list_menu}")
    order = input().lower()
    if order == "off":
        active = False
    elif order == "report":
        coffee_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
