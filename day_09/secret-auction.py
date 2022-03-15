from os import system, name

from logo import logo


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def add_bidder(name, amount):
    global highest_bidder
    transaction = {"name": name, "amount": amount}

    if not highest_bidder:
        highest_bidder = transaction
    elif highest_bidder["amount"] < transaction["amount"]:
        highest_bidder = transaction


print(logo)
done = False
highest_bidder = {}

while not done:
    bidder = input("What is the name of the bidder?: ")
    bid_amount = int(input("How much would you like to bid?: $"))
    add_bidder(bidder, bid_amount)

    should_continue = input("Would you like to add another bid? Y/N\n").lower()
    clear()
    if should_continue == "n":
        done = True
        print(
            f"The winner is {highest_bidder['name']} for ${highest_bidder['amount']}!"
        )
