from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
comp_choice = randint(0, 2)

"1 < 0, 2 < 1, 0 < 2"

player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
)

if player_choice > 2 or player_choice < 0:
    raise ValueError("You chose an invalid number, you lose!")

print(game_images[player_choice])
print("\nComputer chose:")
print(game_images[comp_choice])

if player_choice == comp_choice:
    print("Draw")
elif player_choice - 1 == comp_choice or (player_choice == 0 and comp_choice == 2):
    print("You win!")
else:
    print("You lose!")
