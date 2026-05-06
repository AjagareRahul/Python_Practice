class Empty:
    pass
e=Empty()
e1=Empty()
print(e,e1)

class car:
    def __init__(self):
        print("car created")
c=car()
c1=car()


class Person:
    def __init__(self,name):
        print("hello!!",name)
p=Person('RAHUL')

class Student:
    def __init__(self,name,age):
        print("Hello i am ",name,"and im",age,"years old")
s=Student('Rahul',21)
s1=Student('Amit',22)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__():
        print(self.name,self.age)
p=Person('Rahul',32)
print(f"Name: {p.name} age: {p.age}")

'''
class Test:
    def __init__(self):
        return "Hello"
print(t=Test())
print(t)'''

class Mobile:
    def __init__(self,brand,price):
        print("BRAND:",brand,"PRICE:",price)
m=Mobile('SAMSUNG',20000)
m1=Mobile('APPLE',80000)























