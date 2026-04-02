# Lesson2\3.py
import json
import csv

# with open("./Lesson2/new_data.json", "r") as f:
#     data = json.load(f)

# with open("./Lesson2/data.json", "r") as f:
#     data = json.load(f)

# data = {"person": []}
# data = {[]}
data = []

with open("./Lesson2/list.csv", "r") as f:
    data1 = csv.reader(f)

    for row in data1:
        name, age, city = row
 
        data.append(
            {
                "name": name,
                "age": age,
                "city": city
            }
        )   
        

with open("./Lesson2/new_data.json", "w") as f:
    {json.dump(data, f, indent=4)}   
    


# for n in range(0, 10):
#     print(n)
    
    
# list = [n for n in range(0, 10) if n % 2 == 0]
# print(list)

# list = [n for n in range(0, 10) if n % 2 == 1]
# print(list)

# list = {n for n in range(0, 10) if n % 2 == 1}
# print(list)

# list = (n for n in range(0, 10) if n % 2 == 1)
# print(list)
# # print(list.__getstate__())
# # print(list.__str__())
# # print(list.__init__())

# for item in list:
#     print(item)