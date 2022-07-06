import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

table = {value.letter:value.code for (index, value) in data.iterrows()}

n = input('enter name: ')
n = n.upper()

output_list = [table[letter] for letter in n]
print(output_list)
