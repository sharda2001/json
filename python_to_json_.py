import json
python_obj = {
  'name': "David",
  'class':"I",
  'class': 6  
}
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data)