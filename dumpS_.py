import json
dict1={"name":"shikha",
"age":23,
"topic":"python"
}
string=json.dumps(dict1)
print(string)
print(type(string))