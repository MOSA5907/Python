import os
import sys

# ensure project root is on sys.path so util package can be resolved
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import utility.func as fn
data = fn.read_json()

# data = fn.read_json().sort(key=lambda x: x["department"])  # Sort data by department

# with open("new_data.json", "r") as f:
#     data = json.load(f)
    
print("====================================")
print("-----------  REPORT  ---------------")
print("====================================")
for person in data:
    print("")  
    print(f"---------- Staff Member {data.index(person) + 1} ----------")
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")  
    print(f"Role: {person['role'].capitalize()}")  
    print(f"Department: {person['department'].capitalize()}")  
    print("-----------------------------------")