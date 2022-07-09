import pandas


data = pandas.read_csv('nato_phonetic_alphabet.csv')

table = {value.letter:value.code for (index, value) in data.iterrows()}

while True:
    n = input('enter name: ')
    n = n.upper()

    try:
        output_list = [table[letter] for letter in n]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
        break
