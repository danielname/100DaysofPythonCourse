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

temp_list = data["temp"].to_list()
# channlenge: claculate the average temp in this time period
print(sum(temp_list) / len(temp_list))
print(temp_list)
print(data["temp"].mean())

print(data["temp"].max())

# accessing data in column
print(data["condition"])
print(data.condition)

# accessing data in row
print(data[data.day == "Monday"])

# challenge - pull data from row when temp was max
print(data[data.temp == data.temp.max()])

# accessing specific datum in a row
monday = data[data.day == "Monday"]
print(monday.condition)

print(int(monday.temp) * 9 / 5 + 32)
