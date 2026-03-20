''' A variable is name used to store data in  memory '''
# creating a variable
name = "John"
age = 30
# name --> variable name
# "John" --> value
# age --> variable name
# 30 --> value
# printing the variable
print(name) # output: John
print(age) # output: 30
# we can also change the value of a variable
name = "Jane"
age = 25
print(name) # output: Jane
print(age) # output: 25 
# we can also use the variable in a string
print("My name is " + name + " and I am " + str(age) + " years old.") # output: My name is Jane and I am 25 years old.      

# we can also use the variable in a string using f-string
print(f"My name is {name} and I am {age} years old.") # output: My name is Jane and I am 25 years old.

# we can also use the variable in a string using format method

print("My name is {} and I am {} years old.".format(name, age)) # output: My name is Jane and I am 25 years old.

#multiple_variables 
name, age, city = "John", 30, "New York"
print(name, age, city) # output: John 30 New York
# we can also change the value of multiple variables at once
name, age, city = "Jane", 25, "Los Angeles"
print(name, age, city) # output: Jane 25 Los Angeles
# we can also use the variable in a string using format method
print("My name is {} and I am {} years old. I live in {}.".format(name, age, city)) # output: My name is Jane and I am 25 years old. I live in Los Angeles. 
a=5
a=10
print(a)
 