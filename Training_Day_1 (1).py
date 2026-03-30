# Example: Why Python is called dynamically typed language
# Variable ka datatype automatically decide hota hai (declare karne ki need nahi)
math=40
pi=3.14
name='Swanandi Kayarkar'

print(type(math))
print(type(pi))
print(type(name))

#.................................................

# Example: Typecasting
# Different datatype ko dusre datatype me convert karna

print(2+2)        
print("2"+"2")   

val1=int(input("Enter first value:"))
val2=int(input("Enter second value:"))
print(val1+val2)

#.................................................

# Typecasting to integer

print(int(3.14))
print(int(True))
print(int(False))

# int() complex aur decimal string ko convert nahi kar sakta
# print(int(10+5j))
# print(int("4.22"))

print("4")

#.................................................

# Typecasting to float

print(float(3))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))

# complex number ko float me convert nahi kar sakte
# print(float(50+2j))

#.................................................

# Typecasting to complex

print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
print(complex(5,-3))
print(complex(True,False))

# string ko complex me convert nahi kar sakte agar non-numeric ho
# print(complex("name"))

#.................................................

# Typecasting to Boolean

print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1+2j))
print(bool(0+0j))
print(bool(-1))
print(bool())
print(bool(False))
print(bool(True))

#.................................................

# Program: Simple Interest
p=100000
r=10
t=1

si=(p*r*t)/100
print(si)

#.................................................

# Program: Convert Celsius temperature into Fahrenheit

c=float(input("Enter temp in celcius:"))
f=c*1.8+32

print(float(f))

#.................................................

# Program: Swapping of two numbers using third variable

val1=int(input("Enter first number:"))
val2=int(input("Enter Second number:"))

temp=val1
val1=val2
val2=temp

print("swapped value",val1,val2)

#.................................................

# Alternate swapping method without third variable

a=300
b=100

a=a+b
b=a-b
a=a-b

print(a)
print(b)

#.................................................

# Program: Convert height from feet to inch and centimeter

h=2

inch=h*12
cm=inch*2.54

print(inch)
print(cm)

#.................................................

# Program: Reverse a number

num = 1234567

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10
num = num // 10

d = num % 10
num = num // 10

e = num % 10
num = num // 10

f = num % 10
num = num // 10

g = num % 10

rev = a*1000000 + b*100000 + c*10000 + d*1000 + e*100 + f*10 + g

print(rev)

#.................................................

# HackerRank Problem: Solve Me First

a = int(input())
b = int(input())

print(a + b)

#.................................................

# HackerRank Problem: Simple Array Sum

n = int(input())
arr = list(map(int, input().split()))

print(sum(arr))

#.................................................