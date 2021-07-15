# Choose a difficulty - easy = 10 attempts / hard = 5 attempts

# Set attempts equal to 10 or 5 based on difficulty
# Choose a random number between 1 and 100
# Ask the user to guess a number between 1 and 100
# Display whether the guessed number is higher or lower than the chosen number
# Reduce attempts by 1 on every guess

# Repeat above

# If attempts equals 0, the game ends. The user loses
# if the user guesses the number before 0 attempts, the game ends. The user wins.

from random import randint
from os import system, name
from termcolor import colored

from logo import logo


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def check_guess(user_num, cpu_num):
    if user_num < cpu_num:
        return colored("Too low!\n", "cyan")
    return colored("Too high!\n", "red")


def play_game(guesses):
    print(logo)

    attempts = guesses
    chosen_number = randint(1, 100)
    game_over = False

    print("Guess what number I'm thinking of between 1 and 100!")
    while attempts != 0 and not game_over:
        user_guess = int(input("Guess a number: "))
        attempts -= 1

        if user_guess == chosen_number or attempts == 0:
            game_over = True
        else:
            print(check_guess(user_guess, chosen_number))
            print(f"Attempts: {attempts}")
    if user_guess == chosen_number:
        print(colored(f"\nGreat! You guessed it.", "green"))
    else:
        print(
            colored(
                f"\nYou didn't guess it. Try again! Number: {chosen_number}", "yellow"
            )
        )


while input("Would you like to play? 'y' or 'n': ") == "y":
    difficulty = input("Choose a difficulty. 'easy' or 'hard': ").lower()
    clear()
    if difficulty == "hard":
        play_game(5)
    else:
        play_game(10)
