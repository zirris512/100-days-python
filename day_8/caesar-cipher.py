from collections import deque

from logo import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(text, shift, direction):
    shifted_letters = deque(alphabet)
    shifted_letters.rotate(shift if direction == "decode" else -shift)

    result = ""

    for char in text:
        if char not in alphabet:
            result += char
        else:
            location = alphabet.index(char)
            result += shifted_letters[location]
    return result


done = False
print(logo)

while not done:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    adjusted_shift = shift % len(alphabet)

    print(f"\nThe {direction}d text is {caesar(text, adjusted_shift, direction)}")
    should_repeat = input("Would you like to continue? Y/N\n").lower()
    if should_repeat == "n":
        done = True
        print("\nGoodbye")
