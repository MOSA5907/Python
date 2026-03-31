import json

with open("./Lesson2/data.json", "r") as f:
    data = json.load(f) 

data["person"].append(
    {
        "name": "Moses",
        "age": 66,
        "city": "Accra"
    }
)

# data["person"][0] = {
#             "name": "Moses",
#             "age": 66,
#             "city": "Accra"
#         }

with open("./Lesson2/new_data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("./Lesson2/new_data.json", "r") as f:
    data1 = json.load(f)

print(data1) 
# C:\website\Python\Lesson2\data.json
# Lesson2\data.json