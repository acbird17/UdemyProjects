import csv
import pandas

# with open("./weather_data.csv") as data:
#     weather_data = csv.reader(data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv("./Squirrel_Data.csv")
# print(type(data))
# print(data["temp"])

# data_list = data["temp"].max()

# avg_temp = sum(data_list) / len(data_list)
# monday = data[data.day == "Monday"]
# f_temp = (int(monday.temp) * 9/5) + 32

# print(f_temp)

squirrel_colors = data["Primary Fur Color"]

fur_color_dict = {
    "Gray" : 0,
    "Cinnamon" : 0,
    "Black" : 0,
}

for squirrel in squirrel_colors:
    if squirrel == "Gray":
        fur_color_dict["Gray"] += 1
    if squirrel == "Cinnamon":
        fur_color_dict["Cinnamon"] += 1
    if squirrel == "Black":
        fur_color_dict["Black"] += 1


df = pandas.DataFrame.from_dict(fur_color_dict)
df.to_csv("squirrel_count.csv")
# fur_color_dict.DataFrame.to_csv("../CSVPractice")
# pandas.DataFrame.from_dict(fur_color_dict)        
print(type(fur_color_dict))
print(fur_color_dict)