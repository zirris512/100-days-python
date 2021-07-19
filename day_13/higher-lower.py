# Display logo at the top of every render
# Randomly choose two items from data to compare
# Print information to screen and ask user to pick which one has more followers
# If user picks correctly:
# - Add a point to the user score
# - Remove the item with the lower follower count
# - Add another item to compare to the previous highest follower count
# - *Repeat above while the user continues to guess correctly
# Else:
# - End the game
# - Print the user's final score
# - End program

from random import choice
from os import system, name

from game_data import data
from logo import logo, vs


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


user_score = 0
game_over = False

print(logo)

while not game_over:
    first_item = choice(data)
    second_item = choice(data)

    while first_item["name"] == second_item["name"]:
        second_item = choice(data)

    first_item_followers = first_item["follower_count"]
    second_item_followers = second_item["follower_count"]
    correct_answer = "a" if first_item_followers > second_item_followers else "b"

    print("correct answer...", correct_answer)

    print(
        f"Compare A: {first_item['name']}, a {first_item['description']}, from {first_item['country']}."
    )
    print(f"{vs}")
    print(
        f"Against B: {second_item['name']}, a {second_item['description']}, from {second_item['country']}."
    )

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    clear()
    print(logo)

    if user_guess == correct_answer:
        user_score += 1
        print(f"Correct! Current score: {user_score}")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {user_score}")
