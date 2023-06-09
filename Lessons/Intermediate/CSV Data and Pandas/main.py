# with open("weather_data.csv") as csv:
#     data = csv.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if "temp" not in row:
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data)) #this is a dataframe
# print(type(data["temp"])) #this is a series

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# # channlenge: claculate the average temp in this time period
# print(sum(temp_list) / len(temp_list))
# print(temp_list)
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # accessing data in column
# print(data["condition"])
# print(data.condition)
#
# accessing data in row
print(data[data.day == "Monday"])
#
# # challenge - pull data from row when temp was max
# print(data[data.temp == data.temp.max()])
#
# # accessing specific datum in a row
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# print(int(monday.temp) * 9 / 5 + 32)
#
# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
#
# # creating a new csv file
# new_data.to_csv("new_data.csv")

# squirrel_fur = {
#     "color": ["gray", "cinnamon", "black"],
#     "count": [0, 0, 0]
# }
#
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"].count().X
# squirrel_fur["count"][0] = gray
# cinnamon = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"].count().X
# squirrel_fur["count"][1] = cinnamon
# black = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"].count().X
# squirrel_fur["count"][2] = black
#
# squirrel_csv = pandas.DataFrame(squirrel_fur)
# squirrel_csv.to_csv("squirrel_count.csv")