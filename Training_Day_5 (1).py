# function example
def msg():
    print("hello world")

msg()

#....................................................

# function for addition
def add():
    n1=int(input("Enter the value of n1:"))
    n2=int(input("Enter the value of n2:"))
    print("Add=",n1+n2)

add()

#....................................................

# return multiple values
def multival():
    print("hello world")
    n1=int(input("Enter the value of n1:"))
    n2=int(input("Enter the value of n2:"))
    sum=n1+n2
    mul=n1*n2
    sub=n1-n2
    div=n1/n2
    return sum, sub, mul, div

result=multival()
print(result)

#....................................................

# positional argument
def personalInfo(fname,lname):
    print("First Name=",fname)
    print("Last Name=",lname)

personalInfo("Amrit","Kumar")

#....................................................

# keyword argument
def personalInfo(fname,lname):
    print("First Name=",fname)
    print("Last Name=",lname)

personalInfo(fname="Amrit",lname="Kumar")

#....................................................

# default argument
def cityName(city="Nagpur"):
    print(city)

cityName("Mumbai")
cityName("Delhi")
cityName()   # ✔ error nahi aayega (default value use hogi)

#....................................................

# variable length argument
def studentNames(*name):
    print(name)

studentNames("Amrit","Aman","Rakshit","Aryan","Tejas","Aniket")

#....................................................

# HackerRank: Solve Me First
a = int(input())
b = int(input())
print(a + b)

#....................................................

# HackerRank: Simple Array Sum
n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))

# alternate method
def SimpleArraySum(arr):
    total=0
    for i in range(len(arr)):
        total=total+arr[i]
    return total

#....................................................

# HackerRank: Compare the Triplets 
def compareTriplets(a,b):
    alice=0
    bob=0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
    return [alice,bob]

alice_in=[5,6,7]
bob_in=[3,6,10]

result=compareTriplets(alice_in,bob_in)
print("Scores:",result)

#....................................................

# search element in list
mylist=[5,2,9,7,5,6]

def searchElement(target):
    for i in range(len(mylist)):
        if target==mylist[i]:
            return i
    return -1

result=searchElement(7)

if result!=-1:
   print("Element found at index number=",result)
else:
   print("Element not found")

#....................................................

# A Very Big Sum-HackerRank
def aVeryBigSum(arr):
   return sum(arr)

n=int(input("Enter number of elements:"))
arr = list(map(int, input("Enter numbers: ").split()))

result=aVeryBigSum(arr)
print("The total sum is:",result)

#....................................................

# Time Conversion-HackerRank
def timeConversion(s):
    hour=int(s[:2])
    rest=s[2:8]
    period=s[8:]

    if period=="AM":
        if hour==12:
            hour=0
    else:  # PM
        if hour!=12:
            hour+=12

    return str(hour).zfill(2)+rest

s=input("Enter time (hh:mm:ssAM/PM): ")
print(timeConversion(s))

#....................................................

# Two Sum (LeetCode)
arr1 = [2,7,11,15]

target = int(input("Enter The target value: "))

for i in range(len(arr1)):
    for j in range(i + 1, len(arr1)):
        if arr1[i] + arr1[j] == target:
            print("Indices:", i, j)