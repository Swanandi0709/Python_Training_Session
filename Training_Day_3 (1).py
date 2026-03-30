# Dictionary Example

mydict={
    101:"prasant",
    102:"ashish",
    "103":"mohini",
    "104":"trivani",
    101:"ashish",
    104:"ashish"
}

print(mydict)

# Access value
a=mydict[102]
print(a)

# Update value
mydict[102]="peter"
print(mydict)

# Loop through keys
for x in mydict:
    print(x)

# Loop through key and value
for x,y in mydict.items():
    print(x,y)

# Add new key value
mydict["mobile_no"]=4646463738
print(mydict)

# Remove element
mydict.pop(101)
print(mydict)

#...........................................................

# String slicing

name="prashant"

print(name[0])
print(name[1])
print(name[-1])
print(name[0:5])
print(name[1:])
print(name[:5])
print(name[:])
print(name[1:8:2])
print(name[::-1])

#...........................................................

# find() example
s="h i b l f r p"

print(s.find("h"))
print(s.find("r"))
print(s.find("b"))

#...........................................................

# join example
s=("aman","ashish","sumit")
m="|".join(s)
print(m)

#...........................................................

# String case functions
s="i am great full"

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

#...........................................................

# String formatting
print('subject marks:')

phy=50
chem=60
math=70

print("physics={} chemistry={} math={}".format(phy,chem,math))
print("physics={0} chemistry={1} math={2}".format(phy,chem,math))

total=phy+chem+math
print("total marks",f"{total}")

print("roll no=","7".zfill(4))

#...........................................................

# String checking functions
print('prashantjha777'.isalnum())
print('prashantjha'.isalpha())
print('777'.isdigit())
print('sdsdsdsd'.islower())
print('PRASANT'.isupper())
print('Hello World'.istitle())
print(' '.isspace())
print("hello".startswith("he"))
print("hello".endswith("lo"))

#...........................................................

# Arithmetic expression example
a=50
b=30
c=20
d=10

print((a+b)*c/d)

#...........................................................

# List comparison
x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]

print(x==y)
print(x==z)
print(x!=z)

#...........................................................

# Program: Count vowels and consonants

name="prashant"

count=0
count1=0

for i in name:
    print(i," ",end="")
    
    # corrected vowel condition
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count=count+1
    else:
        count1=count1+1

print()
print("Vowels:",count)
print("Consonants:",count1)
#...............................................................