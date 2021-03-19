a="banana"
b="orange"
#operators will give either true or false as output reason being every character is defined to a number
print(a==b)

#arithmetic operators will combine the characters
print(a+b)
print(a*3)
print("this is Anne\'s spam")

#within astring is quoted it is regarded as a character
x="5"
y="10"
z=x+y
print(z)

print("3"*4)>>>>3333


#indexing strings where b=0 a=1 n=2 a=3 n=4 a=5
s="banana"
letter=s[1]
print(letter)>output is>a

where  b=-6 a-5 n=-4 a=-3 n=-2 a=-1
s="banana"
letter=s[-1]
print(letter)>output is>n

#substring where the output will exclude the first and last character
s="banana"
print(s[1:5])
#output will exclude character from the first on the right towards the left
s="banana"
print(s[-6:-1])
print(s[-5:-1])
print(s[-4:-1])
print(s[-3:-1])
print(s[-2:-1])
print(s[-1:-1])

#finding length of a string
s="banana"
s2="orange"
print(len(s),end=" ")
print(len(s2),end=" ")

#string formating %finding remainder after an integer division
x=20
y=75

print('the sum of %d and %d is %d' % (x, y, x+y))
>>>output>is 20 and 75 is 95

#string formating %finding remainder after an integer division
x=20.33
y=75.76

print('the sum of %f and %f is %f' % (x, y, x+y))
>>>output is>20.33 and 75.76 is 96.90

#string formating %finding remainder after an integer division(s=string)
x="python"
y="programming"

print('the sum of %s and %s is %s' % (x, y, x+y))

#string formating %finding remainder after an integer division with 2 decimal places
x=20.33
y=75.76

print('the sum of %0.2f and %0.2f is %0.2f' % (x, y, x+y))
#string methods used

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

txt = "banana"

x = txt.center(20)

print(x)

txt = "Welcome to my world of python"

x = txt.title()

print(x)

txt = "George has done it"

x = txt.upper()

print(x)


txt = "enough for today"

x = txt.lower()

print(x)

txt = "Welcome to my world"

x = txt.replace("my","our")

print(x)

 

