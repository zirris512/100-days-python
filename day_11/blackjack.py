from os import system, name
from random import choice
from termcolor import colored

from logo import logo


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def deal_card():
    """Return a randomly chosen card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_total, dealer_total):
    """Compares user and dealer totals and returns a winning scenario."""
    if user_total == dealer_total:
        return colored("Draw", "cyan")
    elif dealer_total == 0:
        return colored("Lose, opponent has Blackjack", "red")
    elif user_total == 0:
        return colored("Win with a Blackjack", "green")
    elif user_total > 21:
        return colored("You went over. You lose", "red")
    elif dealer_total > 21:
        return colored("Dealer went over. You win", "green")
    elif user_total > dealer_total:
        return colored("You win", "green")
    return colored("You lose", "red")


def play_game():
    print(logo)

    user_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_deal = input("Type 'hit' to get another card, type 'tap' to pass: ")
            if should_deal == "hit":
                user_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"\n   Your final hand is: {user_cards}, final score: {user_score}")
    print(f"   Dealer hand: {dealer_cards}, dealer score: {dealer_score}\n")
    print(compare(user_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
