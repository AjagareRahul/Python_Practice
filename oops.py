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
