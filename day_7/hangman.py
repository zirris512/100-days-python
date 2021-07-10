from random import choice
from os import system

from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = choice(word_list)
display = ["_" for _ in chosen_word]
end_of_game = False
lives = len(stages) - 1
guesses = []

print(f"{logo}\n")
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    system("clear")

    if guess in guesses or guess in display:
        print("You've already used that letter!")
    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter
    else:
        lives -= 1
        guesses.append(guess)

    print(f"\nGuesses: {' '.join(guesses)}")
    print(stages[lives])
    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You won!")
    elif lives == 0:
        end_of_game = True
        print("You lost!")
