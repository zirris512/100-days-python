import pandas

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        nato_words = [alpha_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_words)


generate_phonetic()
