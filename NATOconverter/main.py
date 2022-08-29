import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_nato():
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please only enter letters")
        generate_nato()
    else:
        print(output)

generate_nato()