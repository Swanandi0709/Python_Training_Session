# import re
var='gasgg54@#vscd!s*'
count=0
for i in var:
    z=ord(i)
    if (97 <= z <= 122) or (48 <= z <= 57):
        continue
    else:
        count+=1

print(count)   # special characters count

#............................................................................

# common elements in 3 arrays
arr1=[1,2,3]
arr2=[2,3,4]
arr3=[3,4,5]

common=set(arr1) & set(arr2) & set(arr3)
result=list(common)
print(result)

# alternate method
result=[]
for i in arr1:
    if i in arr2 and i in arr3:
        result.append(i)
print(result)

#............................................................................

# move zeros to end 
arr=[0,1,0,3,12]

non_zero=[]
zero_count=0

for i in arr:
    if i!=0:
        non_zero.append(i)
    else:
        zero_count+=1

arr = non_zero + [0]*zero_count
print(arr)

#........................................................................

# second largest element
list1=[7,3,9,2,8]

list1.sort()
print(list1)
print(list1[-2])

#............................................................................

# total distance
arr = [10, 11, 7, 12, 14]

def TotalDistance(arr):
    Distance = 0
    for x in range(len(arr) - 1):
        Distance += abs(arr[x] - arr[x+1])
    return Distance

result = TotalDistance(arr)
print(result)

#...............................................................................

# Roy and Profile Picture (HackerEarth)
L = int(input("Enter minimum dimension: "))
N = int(input("Enter number of photos: "))

for _ in range(N):
    W, H = map(int, input().split())

    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")

#......................................................................

# Running Sum of 1D Array
nums = [1,2,3,4]
running_sum=[]

total=0
for i in nums:
    total += i
    running_sum.append(total)

print(running_sum)

#......................................................................

# Palindrome number
class Solution(object):
    def isPalindrome(self,x):
        return str(x) == str(x)[::-1]

# test
obj = Solution()
print(obj.isPalindrome(121))   # True
print(obj.isPalindrome(123))   # False