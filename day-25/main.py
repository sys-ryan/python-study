# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())
# # temp_sum = sum(temp_list)
# # temp_len = len(temp_list)
# # print(f'avg : {temp_sum / temp_len}')
#
# print(data.condition)

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# print(monday)
# print(monday.condition)
#
# data_dict = {
#     "students": ["Ryan", "Apeach", "Park"],
#     "scores": [75, 56, 80]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv('new_data.csv')

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
