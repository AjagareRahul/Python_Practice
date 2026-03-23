# What is loop ?
#Loop is  repeat same code multiple times
#Types of loops in python
#1. for loop
#2. while loop
#for loop
#Syntax of for loop
#for variable in sequence:
    #code to be executed    
#Example of for loop
for i in range(5):
    print(i) #output: 0 1 2 3 4
#while loop
#Syntax of while loop
#while condition:
    #code to be executed
#Example of while loop
i = 0
while i < 5:
    print(i)
    i += 1 #output: 0 1 2 3 4
#Difference between for and while loop
#for loop is used when we know the number of iterations
#while loop is used when we don't know the number of iterations

#Example of for loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) #output: apple banana cherry
#Example of while loop with list
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1 #output: apple banana cherry

#Example of for loop with string
for char in "hello":
    print(char) #output: h e l l o
#Example of while loop with string
s = "hello"
i = 0
while i < len(s):
    print(s[i])
    i += 1 #output: h e l l o
    
for i in range(10,0,-1):
    print(i)