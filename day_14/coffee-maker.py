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
    total_coins = int(input("How many quarters: ")) * 0.25
    total_coins += int(input("How many dimes: ")) * 0.1
    total_coins += int(input("How many nickles: ")) * 0.05
    total_coins += int(input("How many pennies: ")) * 0.01
    return total_coins


def check_resources(current, needed):
    shortage_list = []
    for ingredient in needed:
        if current[ingredient] < needed[ingredient]:
            shortage_list.append(ingredient)
    return shortage_list


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
                for ingredient in chosen_coffee_ingredients:
                    resources[ingredient] -= chosen_coffee_ingredients[ingredient]

                print(f"Here is ${refunded_amount:.2f} in change.")
                print(f"Enjoy your {user_choice}")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            for item in shortages:
                print(f"Sorry, there is not enough {item}")
    else:
        print("Sorry, that is an invalid option.")


