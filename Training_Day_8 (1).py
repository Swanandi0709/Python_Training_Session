# #WAP to perform arithmatic operation using functional programming approach
# #Functions helps us to acheive modularity approach
# import sys
# def addition(num1,num2): # called function
#     print("Addition=",num1+num2)

# def substraction(num1,num2): # called function
#     print("Substraction=",num1-num2)

# def multiplication(num1,num2): # called function
#     print("Multiplication=",num1*num2)

# def division(num1,num2): # called function
#     print("Division=",num1/num2)

# while True:
#     print("1.Addition")
#     print("2.Substraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5.Exit")
#     choice=int(input("Enter your choice from above options:"))
#     if choice==5:
#         sys.exit()
#     val1=int(input("Enter First Value:"))
#     val2=int(input("Enter Second Value:"))
#     if choice==1:
#         addition(val1,val2)
#     elif choice==2:
#         substraction(val1,val2)
#     elif choice==3:
#         multiplication(val1,val2)
#     elif choice==4:
#         division(val1,val2)
#     else:
#         print("You have entered wrong choice")
#..............................................................
# #nested function

# def outerFunction():
#     print("this is my outer function:")#second
#     def innerFunction():
#         print("inner Function")
#     innerFunction()#third
# outerFunction()# first exe start from here
#........................................................
# # input=Amrit is good programmer
# #WAP to count the word
# #output=4
# name="Amrit is a good programmer"
# count=1
# for i in name:
#     if i==" ":
#         count+=1
#     else:
#         continue
# print("Total word count:",count)
#.........................................................
#tupleQuiz MCQ
#Q-1.What will be the output of the following code block?
init_tuple = ()
print(init_tuple.__len__()) #0

#Q-2.What will be the output of the following code block?
init_tuple_a='a','b'
init_tuple_b=('a','b') #() is not mandatory
print(init_tuple_a==init_tuple_b) #True

#Q-3.What will be the output of the following code block?
init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print(init_tuple_a + init_tuple_b) #('1', '2', '3', '4')

#Q-4.What will be the output of the following code block?
l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)

#Q-5.What will be the output of the following code block?
init_tuple = ('Python') * 3
print(type(init_tuple))

#Q-6.What will be the output of the following code block?
#tupple is immutable/non-changeable and list is not
# init_tuple = (1,) * 3      
# init_tuple[0] = 2          
# print(init_tuple)

#Q-7.What will be the output of the following code block?
init_tuple = ((1, 2),) * 7
print(len(init_tuple[3:8]))

#Q-8.What will be the output of the following code block?
# Replacing a string with another string:
# s.replace(oldstring, newstring)
# inside s, every occurrence of oldstring will be replaced with newstring

s = ""
s1 = s.replace("difficult", "easy")
print(s1)
# All occurrences will be replaced
s = "abababababab"
s1 = s.replace("a", "b")
print(s1)
#...............................................................
# Removing spaces from the string:
# 1. rstrip() ===> To remove spaces at right hand side
# 2. lstrip() ===> To remove spaces at left hand side
# 3. strip()  ===> To remove spaces both sides
city = input("Enter your city Name:")
scity = city.strip()
if scity == 'Hyderabad':
    print("Hello Hyderbadi..Adab")
elif scity == 'Chennai':
    print("Hello Madrasi...Vanakkam")
elif scity == "Bangalore":
    print("Hello Kannadiga...Shubhodaya")
else:
    print("your entered city is invalid")
#...............................................................
#list cComprehension:
# Example 1 - Squares
s = [i**2 for i in range(1, 11)]  # i=10
print(s)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example 2 - Powers of 2
val = [2**i for i in range(1, 6)]  # i=5
print(val)
# Output: [2, 4, 8, 16, 32]

# Example 3 - Even numbers from s
val2 = [i for i in s if i % 2 == 0]  # i=1
print(val2)
# Output: [4, 16, 36, 64, 100]
#...........................................................
# Dictionary Comprehension:

squares = {x: x*x for x in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

doubles = {x: 2*x for x in range(1, 6)}
print(doubles)
# Output: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}