'''def grade(a):
    if a>=90:
        return "A"
    elif a>=75:
        print("B")
    elif a>=50:
        print("C")
    else:
        print("Fail")
a=int(input("Enter the number:"))
grade(a)
'''

def show(a,b):
    return a+b
print(show(10,20))

def show(name,sirname):
    return f"Nmae:{name} Sirname:{sirname}"
print(show(name="Rahul",sirname="Ajagare"))

def show(name,age="21"):
    return f"name:{name} age:{age}"
print(show("Rahul"))

def show(*args):
    return sum(args)
print(show(10,30,40))

def show(**data):
    return data
print(show(a=1,b=2,c=3,d=4))

def intro(name,age):
    print(f"Name:{name} age:{age}")
intro(21,"Rahul")
print()
def multiply(a,b,c):
    return a*b*c
print(multiply(10,10,10))
print()
def show(name,age,city="Latur"):
    return f"name:{name} age:{age} city:{city}"
print(show(name="Rahul",age=21))

print()
def show(*number):
    return number
print(show(10,20,30,40))

print()
def show(**data):
    return data
print(show(name="Rahul",age=21,city="Latur"))

def show(*number):
    return sum(number)
print(show(10,20,30,40))


print()
price = 2000
discount = 25

final_price = price - (price * discount / 100)
print(final_price)


def square(x):
    return x*x
print(square(20))

x=10
square=lambda x:x*x
print(square(5))

add=lambda a,b:a+b
print(add(10,30))

even=lambda x:"even" if x%2==0 else "odd"
print(even(1))

numbers=[3,1,4,5,2]
numbers.sort(key=lambda x:x)
print(numbers)



























