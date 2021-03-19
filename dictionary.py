student= {
"Fname": "taiswa",
"Lname": "andy",
"phone":"0722000000",
"email":"kortomtaiswa44@gmail,com"
}
print(student)
+++++++++++++++++++++++++
car ={
"brand":"ford",
"electric":False,
"year":2015,
"colors":["red","white","blue"]
}
print(car)
+++++++++++++++++++++++++
#accessing items in dictionary
x=car["brand"]
print(x)
++++++++++++++++++++++++++++
#accessing items in dictionary
x=car.keys()
print(x)
+++++++++++++++++++++++++++++
#accessing items in dictionary
x=car.values()
print(x
++++++++++++++++++
#existence of key items in dictionary
if "brand" in car:
  print("yes,'brand' is one of the keys in the thisdict dictionary")
++++++++++++++++++++
#existence of key items in dictionary{no output since there is no model key in dict}
if "model" in car:
  print("yes,'model' is one of the keys in the thisdict dictionary")
+++++++++++++++++=
#changing items in dictionary
car ["year"]=2018
print(car)
++++++++++++===
#python add items in dictionary
car["color"]="red"
print(car)
++++++++++++++++++++++++
car ={
"brand":"ford",
"model":"mustang",
"year":2015,
}
#remove items in dictionary
car.pop("model")
print(car)

car.popitem()
print(car)

car.clear()
print(car)

++++++++++++++++++++++++++
car ={
"brand":"ford",
"model":"mustang",
"year":2015,
}
#loopmthrough a dictionary
for x in  car:
 print(x)
for x in  car.values():
 print(x)
+++++++++++++++=
#copy a dictionary
car =car.copy()
print(car)
+++++++++++++++++++++++
#nested dictionaries
toyota ={
"engine1":{
"brand":"probox",
"year":2015,
},
"engine2":{
"brand":"prado",
"year":2016,
},
"engine3":{
"brand":"fielder",
"year":2017,
 }
}
print(toyota)
+++++++++++++++++++++++
#nested dictionaries part2
engine1={
"brand":"probox",
"year":2015,
}
engine2={
"brand":"prado",
"year":2016,
}
engine3={
"brand":"fielder",
"year":2017,
}
toyota={
"engine1":engine1,
"engine2":engine2,
"engine3":engine3,
}
print(toyota)
