# with open("weather_data.csv", 'r') as file:
#     data = file.readlines()
#     print(data)
#
#

# import csv
#
# with open("weather_data.csv", 'r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] == 'temp':
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)


import pandas
data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
temp_list = data["temp"].to_list()
print(temp_list)

# avg = sum(temp_list) / len(temp_list)
# print(avg)

# avg = data["temp"].mean()
# print(avg)
#
# max_val = data["temp"].max()
# print(max_val)
#
#
# print(data.condition)
#
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp
# monday_temp_F = int(monday_temp) * 9/5 + 32
# print(monday_temp_F)
#
# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data = data["Primary Fur Color"]
data = data.value_counts()
data_dict = data.to_dict()

new_data = {
    "Fur Color": [],
    "Count": []
}

for key in data_dict:
    new_data["Fur Color"].append(key)
    new_data["Count"].append(data_dict[key])

new_data = pandas.DataFrame(new_data)
print(new_data)
new_data.to_csv("new_squirrel_data.csv")
