#date:13/3/26

# remove duplicate characters from string
name="prashant"
newname=""
for i in name:
    if i not in newname:
        newname+=i
print("Original:",name)
print("Without duplicate:",newname)

#....................................................

# WAP to reverse the string and check palindrome
name="madam"
newname=""
for i in name:
    newname=i+newname

print("Original:",name)
print("Reverse:",newname)

if name==newname:
    print("It is palindrome")
else:
    print("It is not palindrome")

# another method
print("Reverse using slicing:",name[::-1])

#....................................................

# Anagram program
word1="listen"
word2="silent"

if sorted(word1)==sorted(word2):
    print("It is Anagram")
else:
    print("It is not Anagram")

#....................................................

# continue example
mycart=[10,20,200,300,800,60,700]

for i in mycart:
    if i>400:
        print("this my purchased cart items")
        continue
    print(i)

#....................................................

# Dictionary operations

mydict={"name":"Prashant","age":25}

# add key-value pair
mydict["city"]="Nagpur"
print(mydict)

# remove key-value pair
mydict.pop("age")
print(mydict)

# check key exist
if "name" in mydict:
    print("key exist")

# iterate dictionary
for k,v in mydict.items():
    print(k,v)

#....................................................

# nested for loop for matrix
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

#....................................................

# alphabet matrix pattern
n=int(input("enter the number of row:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()

#....................................................

# corrected number pattern (error fixed)
n=int(input("enter the number of row:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
    print()

#....................................................

# decreasing alphabet pattern
n=int(input("enter the number of row:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+i),end=" ")
    print()

#....................................................

# break example
for i in range(1,5):
    if i==3:
        break
    print(i)

#....................................................

# use two iteration forloop at a time
for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i," ",j)

#....................................................

# while loop example
i=1
while i<=5:
    print(i)
    i=i+1

#....................................................

# password check question
username=""
password=""

while username!="admin" or password!="hello":
    username=input("enter username:")
    password=input("enter password:")

print("Login successful")

#....................................................

# sum of first n numbers
n=int(input("enter number:"))
sum=0
i=1

while i<=n:
    sum=sum+i
    i=i+1

print("the sum of first",n,"number is:",sum)

#....................................................