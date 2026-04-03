# Lesson2\3.py
import json
import csv


def read_json():
    
    data = []   
   
    with open("./Lesson2/list.csv", "r") as f:
        data1 = csv.reader(f)

        for row in data1:
            name, age, city, role, department = row
    
            data.append(
                {
                    "name": name,
                    "age": age,
                    "city": city,
                    "role": role,
                    "department": department
                }
            )   
            
    with open("./Lesson2/new_data.json", "w") as f:
        {json.dump(data, f, indent=4)}   
    
    return data

if __name__ == "__main__":
    read_json() 