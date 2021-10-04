import json
list={"shopping_list":{"choco":"15","biscuits":"50","diary_milk":"30","ice_cream":"20"}}
item=input("enter the item: ")
number=int(input("enter the quantity: "))
a=list["shopping_list"][item]
rem=int(a)-number
list["shopping_list"][item]=rem
b=json.dumps(list)
print(b)

