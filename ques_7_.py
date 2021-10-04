import json
dic={}
with open("my_file.txt") as f:
    for line in f:
        key,value=line.strip().split(None,1)
        dic[key]=value.strip()
file=open("7que.json","w")
json.dump(dic,file,indent=4)
print(json.dumps(dic,indent=4))
file.close()

# import json
# file=open("my_file.txt","r")
# data=file.read()
# # print(da
# dic={}
# for line in data:
#     key,value

