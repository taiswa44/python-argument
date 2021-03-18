# if else statement
i = 20
if(i>10):
     print("10 is less than 15")
else:
   print("i is greater thn 10")
  ++++++++++++++++++++++++++++
#shows if number is even or odd.
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("is Even")
else:
   print(" is Odd")
++++++++++++++++++++++++++++++++++
num = 7
# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
++++++++++++++++++++++++++++++++++++++++
print("Enter Marks Obtained in 5 Subjects: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e= int(input())

sum = a+b+c+d+e
print(sum)
avg = sum/5
print(sum/5)

if avg>=81 and avg<=100:
    print("Your Grade is A")

elif avg>=61 and avg<81:
    print("Your Grade is B")

elif avg>=41 and avg<61:
    print("Your Grade is C")

elif avg>=21 and avg<41:
    print("Your Grade is D")

elif avg>=0 and avg<21:
    print("Your Grade is E")
else:
    print("Invalid Input!")
