"""Coffee Machine Code.
Project for Angela Wu's 100 days of code challenges.
Day # 15
"""
from data import MENU, resources

money = 0
current_resources = resources.copy()


def report(lasting_resources: dict):
    """Display a report of resources and money in the coffee machine."""
    print(f'Water: {lasting_resources["water"]}ml.')
    print(f'Milk: {lasting_resources["milk"]}ml.')
    print(f'Coffee: {lasting_resources["coffee"]}g.')
    print(f'Money: ${money}')


def user_choice():
    """Prompts the menu for the coffee machine and returns the selection from menu."""
    menu = """\nChoose your drink: 
    1.- ESPRESSO
    2.- LATTE
    3.- CAPPUCCINO
    """
    print(menu)
    answer = input().lower()
    while (answer != "1" and answer != "2" and answer != "3"
           and answer != "report" and answer != "off"):
        answer = input(menu)
    if answer == "1":
        answer = "espresso"
    if answer == "2":
        answer = "latte"
    if answer == "3":
        answer = "cappuccino"
    return answer


def check_resources(order: str, lasting_resources: dict):
    """Check if there are enough resources to prepare the customer's drink."""
    order_ingredients = MENU[order]['ingredients']
    for ingredient in order_ingredients:
        if lasting_resources[ingredient] - order_ingredients[ingredient] < 0:
            print(f"Sorry, there's not enough {ingredient}")
            return False
        else:
            return True


def charge(order, cost):
    """Charges the coffee and update the money with the inserted coins."""
    print(f"Your {order} costs ${cost}. Please insert coins.")

    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total_inserted = quarters + dimes + nickles + pennies

    return total_inserted


def make_drink(order: str, lasting_resources: dict):
    """Makes the drink and update the current resources on the machine."""
    order_ingredients = MENU[order]['ingredients']
    for k, v in order_ingredients.items():
        lasting_resources[k] -= v
    print(f"Here's your {order.upper()}")


active = True

while active:
    # Order drink
    order = user_choice()

    if order == "off":
        print("Shutting down the machine for maintenance and re-filling.")
        active = False

    elif order == "report":
        report(lasting_resources=current_resources)

    else:  # Check, resources, charge and deliver drink
        drink_cost = MENU[order]["cost"]
        # Check
        check = check_resources(order=order, lasting_resources=current_resources)
        if check:
            # Charge
            pay = charge(order=order, cost=drink_cost)
            if pay < drink_cost:
                print(f"Sorry, there's not enough for your drink. Here is your refund of ${pay}")
            else:
                if pay > drink_cost:  # Give change
                    print(f"Here's ${round(pay - drink_cost,2)} in change")
                money += drink_cost  # Adds money to the machine
                make_drink(order=order, lasting_resources=current_resources)