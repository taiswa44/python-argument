print('Hello, world!')
def my_function():
 print("Hello world")
my_function()
#SUM
def sum(x,y):
  a=x+y
  print("The Sum is ",a)

sum(10,20)
sum(501,958)
def Sum(x,y,z):
     a=x+y+z
     return a
print(sum(10,20,30))
#argument
def courses(*args):
   for subject in args:
    print(subject)
courses("Big Data","CCNA","OOP2")