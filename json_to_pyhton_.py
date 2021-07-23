import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"])



# j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
# print("Original String:")
# print(j_str)
# print("\nJSON data:")
# print(json.dumps(j_str, sort_keys=True, indent=4))