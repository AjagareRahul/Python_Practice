class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price #instance variable

    def app_disc(self,percent):
        if percent >0 and percent<50:
            self.price=self.price-(percent/100*self.price)
        else:
            print("invalid discount")
    def __str__(self):
        return f"Product:{self.name} Price:{self.price}"
            
p=Product("Laptop",1000)
p.app_disc(10)
p2=Product("Mobile",29894)
p2.app_disc(10)
print(f"Prduct:{p2.name} Price:{p2.price}")
print(p)
print()
class Employees:
    total_salary=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def add_salary(self):
        Employees.total_salary+=self.salary

e=Employees("Rahul",32000)
e.add_salary()
e2=Employees("Rajeev",8000)
e2.add_salary()
print(f"Name:{e.name} Salary:{e.salary}")
print(f"Name:{e2.name} Salary:{e2.salary}")
print("Total-Salary:",Employees.total_salary)
print()
class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.attempts=3

    def login(self,u,p):
        if self.attempts==0:
            print("Account Locked")
            return
        if self.username==u and self.password==p:
            print("Login Success!")
            self.attempts=3
            
        else:
            self.attempts -=1
            print(f"Wrong Try Again {self.attempts} attempts are left")
            if self.attempts==0:
                print("Account Locked")

u=User("Rahul",123)
u.login("Rahul",145)
u.login("Rahul",123)
u.login("Rahul",145)
u.login("Rahul",145)
u.login("Rahul",123)
print()
class Wheel:
    wheels=4
    def __init__(self,wheels):
        Wheel.wheels=wheels

    def show(self):
        print(self.wheels)



w=Wheel(wheels=6)
w.show()
w2=Wheel(5)
w2.show()
            
            










        
    
        


