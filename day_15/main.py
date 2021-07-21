from os import system, name

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


coffee_items = Menu()
maker = CoffeeMaker()
cash_machine = MoneyMachine()
is_on = True

while is_on:
    user_choice = input(f"What would you like? ({coffee_items.get_items()}): ").lower()
    clear()

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        maker.report()
        cash_machine.report()
    else:
        coffee_item = coffee_items.find_drink(user_choice)
        if coffee_item:
            if maker.is_resource_sufficient(coffee_item) and cash_machine.make_payment(
                coffee_item.cost
            ):
                maker.make_coffee(coffee_item)
