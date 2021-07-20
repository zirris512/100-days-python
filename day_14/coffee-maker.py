from os import system, name

from resources import MENU, resources

turn_off = False
total_in_machine = 0


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def show_report():
    print(f"Water: {resources['water']}mL")
    print(f"Milk: {resources['milk']}mL")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_in_machine:.2f}")


def add_money():
    quarters = float(input("How many quarters: ")) * 0.25
    dimes = float(input("How many dimes: ")) * 0.1
    nickles = float(input("How many nickles: ")) * 0.05
    pennies = float(input("How many pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_resources(current, needed):
    is_not_enough = []
    if current["water"] < needed["water"]:
        is_not_enough.append("water")
    if current["milk"] < needed["milk"]:
        is_not_enough.append("milk")
    if current["coffee"] < needed["coffee"]:
        is_not_enough.append("coffee")
    return is_not_enough


while not turn_off:
    user_choice = input("What would you like? (espresso, latte, cappuccino) ").lower()
    clear()

    if user_choice == "report":
        show_report()
    elif user_choice == "off":
        turn_off = True
    elif user_choice in MENU:
        chosen_coffee_cost = MENU[user_choice]["cost"]
        chosen_coffee_ingredients = MENU[user_choice]["ingredients"]
        shortages = check_resources(resources, chosen_coffee_ingredients)

        if len(shortages) == 0:
            print("Please insert coins.")
            total_money = add_money()
            if total_money > chosen_coffee_cost:
                refunded_amount = total_money - chosen_coffee_cost
                total_in_machine += chosen_coffee_cost
                resources["water"] -= chosen_coffee_ingredients["water"]
                resources["milk"] -= chosen_coffee_ingredients["milk"]
                resources["coffee"] -= chosen_coffee_ingredients["coffee"]

                print(f"Here is ${refunded_amount:.2f} in change.")
                print(f"Enjoy your {user_choice}")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            for item in shortages:
                print(f"Sorry, there is not enough {item}")
    else:
        print("Sorry, that is an invalid option.")


