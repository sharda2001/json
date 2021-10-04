import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"] 
e=["name","destination","age","salary"]
user=input("enter the emp: ")
dic1={}
dic2={}
dic3={}
dic4={}
dic={}
i=0
while i<len(a):
    j=0
    while j<len(a):
        dic1[e[i]]=a[i]
        dic2[e[i]]=b[i]
        dic3[e[i]]=c[i]
        dic4[e[i]]=d[i]
        j=j+1
    dic["emp1"]=dic1
    dic["emp2"]=dic2
    dic["emp3"]=dic3
    dic["emp4"]=dic4
    i=i+1
print(dic)
f=open("saralques8.json","w")
j=json.dump(dic,f,indent=4)
print(type(j))