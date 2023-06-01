# with open("weather_data.csv") as csv:
#     data = csv.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if "temp" not in row:
            temperatures.append(int(row[1]))
    print(temperatures)
