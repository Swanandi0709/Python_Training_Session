# Q-10 What will be the output of the following code snippet
fruit_list1=['Apple','Berry','Cherry','Papaya']
fruit_list2=fruit_list1
fruit_list3=fruit_list1[:]   # copy

fruit_list2[0]='Guava'
fruit_list3[1]='Kiwi'

sum=0
for ls in (fruit_list1,fruit_list2,fruit_list3):
    if ls[0]=='Guava':
        sum+=1
    if ls[1]=='Kiwi':
        sum+=20

print(sum)   # Output: 22

#....................................................................

# Q-8 Default mutable argument 
def f(i,values=None):
    if values is None:
        values=[]
    values.append(i)
    print(values)

f(1)
f(2)
f(3)

#....................................................................

# Function argument behavior
def func(value,values):
    var=1
    values[0]=44

t=3
v=[1,2,3]

func(t,v)
print(t,v[0])   # Output: 3 44

#....................................................................

# Dictionary sorting
dict1={'c':97,'a':96,'b':98}
for key in sorted(dict1):
    print(dict1[key])

#....................................................................

# Fruit dictionary count
fruit={}
def addone(index):
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1

addone('Apple')
addone('Banana')
addone('apple')

print(len(fruit))   # Output: 3

#....................................................................

# Product of Array Except Self-Leetcode
def productExceptSelf(nums):
    n = len(nums)
    result = [1]*n

    # left pass
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # right pass
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result

nums = [1,2,3,4]
print(productExceptSelf(nums))   # Output: [24, 12, 8, 6]

#....................................................................