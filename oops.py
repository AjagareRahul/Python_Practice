'''class person:
    def __init__(self,c,y):
        self.name="Rahul"
        self.age=18
        self.course=c
        self.year=y
    def __str__(self):
        return 'This is person'
person1=person("BCS",2025)
person2=person("BCA",2025)

print(person1.course,person1.year)
print(person2.course,person2.year)

print(person2.name,person2.age)
print(person2)
print(person1)

class person:
    def __init__(self,name,age,course,year,city):
        self.name=name
        self.age=age
        self.course=course
        self.year=year
        self.city=city
    def __str__(self):
        return f"Name:{self.name},age:{self.age},course:{self.course},year:{self.year},city:{self.city}"
person1=person("Rahul",18,'BCA',1,'Pune')
print(person1)
from Variables import name


class Person:
    country='Indian'
    def __init__(self,name):
        self.name=name

person=Person("Rahul")
person2=Person("Rajeev")
person.country="USA"
print(person2.country)
print(person2.name)
print(person.country)
print(person.name)
from html.entities import name2codepoint


class Employee:
    company="TCS"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return f"Name:{self.name},salary:{self.salary},company:{Employee.company}"
emp=Employee("Rahul",89000)
emp.company="WIPRO"
print(emp)
print(emp.company)'''
import math


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(f"Name:{self.name},salary:{self.salary}")

emp=Employee("Rahul",89000)
emp.show()

class Employee:
    company="TCS"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company_name(cls,new_name):
        cls.company=new_name
print(Employee.company)
Employee.change_company_name("Infosys")
print(Employee.company)


class Employee:
    @staticmethod
    def greet():
        print("Welcome to Employee")
Employee.greet()

class Student():
    school="Netaji Vidyalaya"
    def __init__(self,name):
        self.name=name

class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
s1=Student("Rajeev")
s1.display()
s2=Student("Rajeev")
s2.display()

class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
c1=Car("BMW",50000)
print(c1.brand,c1.price)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e1=Employee("Rajeev",40000)
e2=Employee("Rajeev",50000)
print(e1.name,e1.salary)
print(e2.name,e2.salary)
print()
print()
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount

acc=BankAccount("RAHUL",1000)
acc.deposit(100)
acc.withdraw(10)
print(acc.balance)

class Laptop:
    brand="HP"
l1=Laptop()
l2=Laptop()
print(l1.brand,l2.brand)
Laptop.brand="DELL"
print(Laptop.brand)
print(l1.brand,l2.brand)


print()
print()
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_pass(self):
        return self.marks>=40
s1=Student("Rajeev",45)
print(s1.is_pass())

print()
print()
class Rectangle:
    def __init__(self,length,width):
        self.width=length
        self.height=width
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
r=Rectangle(10,20)
print(r.area())
print(r.perimeter())
print()
print()
class Employee:
    count=0
    def __init__(self):
        Employee.count+=1
e1=Employee()
e2=Employee()
e3=Employee()
print(Employee.count)

class Account:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount>(self.balance):
            print("Insufficient Balance")
        else:
            return  f"self.balance-=amount"
a=Account(1000)
a.withdraw(100)
print(a.balance)
print()
class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    def apply_discount(self,percent):
        self.price=self.price-(self.price*percent/100)
book=Book("LOVER",1000)
book.apply_discount(10)
print(book.price)

print()

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def circumference(self):
        return 2*math.pi*self.radius
    def volume(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
circle=Circle(5)
print(circle.area())
print(circle.volume())
print()
class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def check_login(self,u,p):
        return u==self.username and p==self.password
user1=User("Rajeev","123")
print(user1.check_login("Rajeev","123"))
print()

class Product:
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity
    def sell(self,q):
        if self.quantity:
            self.quantity-=q
        if self.quantity<0:
              
p=Product("Rajeev",5)
p.sell(10)
print(p.quantity)
print(p.name,p.quantity)


