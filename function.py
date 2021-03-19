#python functions
def my_function():
  print("hello world")
  
my_function()
++++++++++++++++++++++++++++++++++
#arguments
def sum(x,y):
  a=x+y
  print("the sum is",a)
sum(10,20)
sum(501,950)
+++++++++++++++++++++++++++++++
#arguments
def product(v,w):
  b=v*w
  print("the product is",b)
product(10,20)
product(501,950)
++++++++++++++++++++++++++
#arguments
def sum(c,d):
  e=c+d
  return e
print(sum(10,20))
+++++++++++++++++++++++++++++
 number of arguments
def courses(*args):
  for subject in args:
    print(subject)
courses("big data","ccna","oop2")  
+++++++++++++++++++++++++++
#arguments
def courses(*args):
  for subject in args:
    return subject
print(courses("OSAAD","ccna","OOP2"))
+++++++++++++++++++++++++++++++
#arbitrary keyword arguments

def courses(**kwargs):
  for key,value in kwargs.items():
    print("{}:{}".format(key,value))
courses(first='Big data',second='CCNA',third="hcia")    
++++++++++++++++++++++++++++++++++++
#default parameters
def kenya(County="Mombasa"):
  print("I am from" + County)
kenya()
kenya("nairobi")
kenya("kiambu")
kenya("kisumu")
++++++++++++++++++++++++++++++++++
#passing a list
def my_function(food):
  for x in food:
    print(x)
fruits =["apple","banana","cherry"]
my_function(fruits)
+++++++++++++++++++++++++++++++++++++++===
#passing a list
def my_function(food):
  for x in food:
    print(x)
fruits =["apple","banana","cherry"]
my_function(fruits)

#for dictionaries to pass a list
def my_function(student):
  for y in student:
    print(y)
student= {
"Fname": "george",
"Lname": "andy",
"phone":"0722000000",
"email":"georgeandy@gmail.com"
}
my_function(student)
++++++++++++++++++++++++++++++++
#pass statement
(area of a circle,volume of a cylinder,area of a rectangle,
grading sysytem,volume of asphere)
area = P*r2

def areacircle(radius,radius):
    P= 3.14159
    area = PI*radius *2
 print("the area is",area)
 area(10,10)
++++++++++++++++++++++++++++++
def rectanglearea(width,height):
 area=width*height
 print("the area is",area)
rectanglearea(20,50)

+++++++++++++++++++++++
def circlearea(radius):
  PI=3.142
  area=PI*(radius**2)
  print("the area is",area)
circlearea(5)



