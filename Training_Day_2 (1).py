# Example of Python List and basic list operations

# Creating a list with different data types (string + integer)
mylist=["Amrit","Govind","Aniket","Tejas","Ashish","Aryan","Sandeep",77,56,"Aman"]

# print complete list
print(mylist)

# check datatype of list
print(type(mylist))

# access elements using index
print(mylist[0])   
print(mylist[1])   
print(mylist[2])   

# negative indexing (last element)
print(mylist[-1])

# slicing list
print(mylist[2:5])   # elements from index 2 to 4
print(mylist[:5])    # elements from start to index 4
print(mylist[1:])    # elements from index 1 to end
print(mylist[1:8:2]) # step slicing (skip 1 element)
print(mylist[:])     # print complete list
print(mylist[::-1])  # reverse the list

#...................................................................................

# use append() → add element at last of list
mylist.append('harsh')
mylist.append('lakshman')
print(mylist)

#....................................................................................

# use insert() → add element at specific index
mylist.insert(1,"Sanket")
print(mylist)

#.....................................................................................

# use remove() → remove element by value
mylist.remove("Sandeep")
print(mylist)

#......................................................................................

# copy() → cloning list (create new copy)
newlist=mylist.copy()
print(mylist)
print(newlist)

#......................................................................................

# Multidimensional list example (list inside list)
mylist=[['Amrit','Aryan'],['85.86'],[440022,"yyy"]]

print("Example of multidimensional list:")

# accessing elements using row and column index
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])

#........................................................................................

# list repetition using * operator
list1=["Amrit","Aryan"]
print(list1*2)

# list concatenation using + operator
list2=[50,25.50]
print(list1+list2)

#........................................................................................

# delete element example
list3=[50,25.50,'Amrit']
del list3[2]
print(list3)

# delete entire list
del list3
# print(list3)  # error because list is deleted

#........................................................................................

# clear() → remove all elements from list
list4=[50,25.50,'Amrit']
list4.clear()
print(list4)

#........................................................................................

# typecasting string to list
name="Amrit"
print(name)
myname=list(name)
print(myname)

#........................................................................................

# sorting example
mylist=[44,22,77,0,9,88]
mylist.sort()
print(mylist)

# default sorting:
# numbers → ascending order
# strings → alphabetical order
# list should contain same datatype otherwise TypeError

#........................................................................................

# id() function example (memory address check)
math=50
physics=50
eng=40

print(id(math))
print(id(physics))
print(id(eng))

#........................................................................................

# aliasing concept (two variables pointing to same list)
mylist=[44,22,77,0,9,88]
newlist=mylist

print(id(mylist))
print(id(newlist))

#........................................................................................

# membership operator example (in / not in)
name='Amrit'

print('Z' in name)
print('Z' not in name)

#........................................................................................

# loop examples using range()

for i in range(1,10,2):
    print(i)

for i in range(5,0,-1):
    print(i)

#print multiplication table of 2
for i in range(1,11):
    print(i*2)

#........................................................................................

# print multiplication tables from 2 to 20
for i in range(1,11):
    print(i*2 , " ",i*3 ," ", i*4 ," ", i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)

print(".....................")

for i in range(1,11):
    print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)

#...............................................................................................

# WAP to accept number and check positive, negative or zero
no=int(input("Enter any digit:"))

if no>0:
    print('positive')

if no<0:
    print("negative")

if no==0:
    print("zero")

#.................................................................................................

# WAP to accept day and check working day or weekend
days=input("Enter day:")

if(days=="Monday" or days=="Tuesday" or days=="Wednesday" or days=="Thursday" or days=="Friday"):
    print("Working Days")

elif(days=="Saturday" or days=="Sunday"):
    print("Weekend")

#................................................................................................

# WAP to accept three paper marks and calculate total and percentage
# and check eligibility for placement

Paper1=int(input("Enter marks:"))
Paper2=int(input("Enter marks:"))
Paper3=int(input("Enter marks:"))

total=Paper1 + Paper2 + Paper3
print(total)

percentage=total/3
print(percentage)

if(percentage>=60):
    print("He/She is eligible for placement")
else:
    print("not eligible for placement")

#................................................................................................

# WAP to accept five values and find maximum value using simple if

var1=int(input("Enter 1st var:"))
var2=int(input("Enter 2nd var:"))
var3=int(input("Enter 3rd var:"))
var4=int(input("Enter 4th var:"))
var5=int(input("Enter 5th var:"))

if var1> var2 and var1>var3 and var1>var4 and var1>var5:
    print("Var1 is greater")

if var2> var1 and var2>var3 and var2>var4 and var2>var5:
    print("Var2 is greater")

if var3> var1 and var3>var2 and var3>var4 and var3>var5:
    print("Var3 is greater")

if var4> var1 and var4>var2 and var4>var3 and var4>var5:
    print("Var4 is greater")

if var5> var1 and var5>var3 and var5>var4 and var5>var2:
    print("Var5 is greater")
#................................................................................................