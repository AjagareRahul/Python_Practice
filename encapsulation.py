class Bank:
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")
b=Bank(1000)
b.deposit(500)
b.withdraw(200)
print(b.get_balance())


class Account:
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")

a=Account(1000)
a.deposit(500)
a.withdraw(200)
print(a.get_balance())


class Utils:
    @staticmethod
    def is_even(num):
        return num%2==0

print(Utils.is_even(4))
print(Utils.is_even(7))


print()

class Utils:
    @staticmethod
    def is_odd(num):
        return num%2!=0
print(Utils.is_odd(4))
print(Utils.is_odd(7))


print()
class Utils:
    @staticmethod
    def square(num):
        return num*num
print(Utils.square(9))
print()
class Company:
    name='TCS'
    @classmethod
    def change_name(cls,new_name):
        cls.name=new_name
        return cls.name

    
print(Company.change_name('WIPRO'))
print(Company.name)
print()
class Utils:
    @staticmethod
    def is_positive(num):
        return num>0
print(Utils.is_positive(8))
print(Utils.is_positive(-20))

print()

class Employee:
    company="Infosys"

    @classmethod
    def change_company(cls,name):
        cls.company=name

    @staticmethod
    def is_valid_salary(salary):
        return salary>0

print(Employee.change_company("TCS"))

print()

class Company:
    name='TCS'

    @classmethod
    def change_name(cls,new_name):
        cls.name=new_name
        return cls.name

print(Company.change_name('Wipro'))
print()
class Student:
    count=0
    def __init__(self):
        Student.count +=1
s=Student()
s1=Student()
s3=Student()
print(Student.count)
print()
class Utils:
    @staticmethod
    def is_positive(num):
        print(num>0)

Utils.is_positive(90)
print()
class Employees:
    company='Infosys'
    @classmethod
    def change_company(cls,name):
        cls.company=name
        return cls.company

    @staticmethod
    def is_valid_salary(salary):
        return salary>0


print(Employees.change_company('TCS'))
print(Employees.is_valid_salary(8))

print("class and object")
class Bank:
    bank_name='SBI'
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name=name
        return f"New Bank:{cls.bank_name}"

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

    def show(self):
          return f"Name:{self.name} Total Balance:{self.balance}"

acc=Bank('Rahul',89700)
print(Bank.change_bank_name('RBI'))
print(f"My Balance:{acc.balance}")
acc.deposit(300)
print(acc.show())
print()
acc2=Bank('Rajiv',85700)
print(Bank.change_bank_name('AXIX'))
print(f"My Balance:{acc2.balance}")
acc2.deposit(300)
print(acc2.show())
        










        
        














































    
        
