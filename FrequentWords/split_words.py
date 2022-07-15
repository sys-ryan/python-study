import pandas
import pandas as pd

data = pd.read_csv('data.csv')

print(data.Word)
data_list = data.Word.to_list()
print(data_list)

new_data = {
    "Word": []
}

for word in data_list:
    voca = word.split(" ")[0]
    new_data["Word"].append(voca)

new_data = pandas.DataFrame(new_data)
print(new_data)

new_data.to_csv("filtered_data.csv")