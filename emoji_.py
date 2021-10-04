import json
from typing import List
file1 = open("emoji.json")
intr= json.load(file1)
list=[]
list1=[]
i=1
for i in intr:
   list.append(i["title"])
   list1.append(i["symbol"])
a=list
b=list1
dict={}
res = {a[i]:b[i] for i in range(len(a))}
user=input("enter the title")
for i in res:
    if user==i:
        print(res[i])