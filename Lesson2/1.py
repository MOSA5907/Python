import json

with open("./Lesson2/data.json", "r") as f:
    data = json.load(f) 

# Print all keys in the data
print("Print all keys in the data")
print(data)
for key, list in data.items():
    print(f"{key}: {list}")
    
    for key1, value1 in list.items():
        print(f"{key1}: {value1}")

print("------------------------------")
   
# Print all values in the data 
print("Print all values in the data")
print(data["person"][0])
for key, value in data["person"][0].items():
    print(f"{key}: {value}")

print("------------------------------")
   
# Print all names, ages, and cities in the data
print("Print all names, ages, and cities in the data")
print(data["person"])
for i in data["person"]:
    print(i["name"])
    print(i["age"])
    print(i["city"])

# for name, age, city in data["person"]:
#     print(f"{name}: {age}, {city}")

    # data["person"].append(
    #     {
    #         "name": name,
    #         "age": age,
    #         "city": city
    #     }
    # )

# with open("./Lesson2/new_data.json", "w") as f:
#     json.dump(data, f, indent=4)

# with open("./Lesson2/new_data.json", "r") as f:
#     data = json.load(f)

# print(data) 
# C:\website\Python\Lesson2\data.json
# Lesson2\data.json