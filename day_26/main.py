import pandas

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}

user_word = input("Enter a word: ").upper()
nato_words = [alpha_dict[letter] for letter in user_word]

print(nato_words)
