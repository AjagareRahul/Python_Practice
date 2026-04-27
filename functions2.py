def show():
    return "hello Danny"
print(show())
'''
def show(n):
    for i in range(1,n+1):
        print(i)
n=int(input("Enter the number:"))
show(n)'''

def show(s):
    return s*s
print(show(5))

def show(a,b):
    return a+b
print(show(10,20))

def show(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")

show(6)

def show(a,b):
    if a>b:
        print("A is greater")
    else:
        print("B is greater")
show(39,32)
print()
print()
l=[1,2,3,4,5,6]
def show(l):
    count=0
    for i in l:
        count=i
    print(count)
show(l)
l=[1,2,3,4,5,6,7,8,9]
def show(l):
    result=0
    for i in l:
        result+=i
    print(result)
show(l)

l=[1,2,3,4,5,6,7]
def show(l):
    result=0
    for i in l:
        result+=i
    print(result,result/len(l))
show(l)

def show(name="Guest"):
    return name
print(show())


def show(x,y=2):
    return x**y
print(show(10))

def order(item,quantity=1):
    return item,quantity
print(order("Cement"))

def profile(name,age=18,city="Unknown"):
    return f"name:{name} age:{age} city:{city}"

print(profile("Rahul"))


def order(item,quantity=1):
    return f"{quantity} {item}(s) ordered"
print(order("Cement"))

def add(*numbers):
    total=0
    for i in numbers:
        total+=i
    return total
print(add(1,2,3))
print(add(43,34,34))

def show(a,*n):
    print("a:",a)
    print("n:",n)
show("Rahul",1,2,3,4)


def info(**data):
    return data
print(info(name="Rahul",sirname="Ajagare"))


def info(**data):
    for key,value in data.items():
        print(key,"=",value)
info(name="Danny",age=22)

def demo(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)
demo(10,20,30,name="Danny",age=22)
print()
def create_user(name,**extra):
    user={"name:":name}
    user.update(extra)
    return user
print(create_user("Danny",age=22,city="Pune"))

def sam(*numbers):
    return sum(numbers)
print(sam(1,2,3,4,5))

print()
def show(**data):
    return data
print(show(name="Danny",age="22",city="Latur"))
print()
def student(name,*marks,**info):
    return {"Name":name,"Total_Marks":marks,"info":info
        }
print(student("Rahul",90,80,50,60,age=22,city="Latur"))
print()

def test():
    x=10
    print(x)
test()

x=20
def test():
    print(x)
test()

print()
x=20
def test():
    x=10
    print(x)
test()
print(x)
print()
x=10
def change():
    global x
    x=50
change()
print(x)


#lambda arguments:expression
square=lambda x:x*x
print(square(5))


print()
add=lambda a,b:a+b
print(add(10,30))

print()
even_odd=lambda x:"Even" if x %2==0 else "Odd"
print(even_odd(43))

print()
nums=[1,2,3,4,5]
result=list(map(lambda x:x*2,nums))
print(result)
print()
x=20
def show():
    x=30
    print("Local:",x)
show()
print("Global:",x)

print()
x=20
def show():
    global x
    print("Accessing global variable to local:",x)
    x=50
show()
print(x)

cube=lambda x:x*x*x
print(cube(5))
e_o=lambda x:"Even" if x%2==0 else "Odd"
print(e_o(5))

print()
def even(n):
    return "Even" if n%2== 0 else "Odd"
print(even(6))


print()
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))

print()
def maximum(a,b,c):
    return max(a,b,c)
print(maximum(10,30,40))

print()
def count_vowels(s):
    count=0
    for i in s.lower():
        if i in "aeiou":
            count+=1
    return count
print(count_vowels("Rahul"))
square=lambda x:x*x
print(square(6))
print()
cube=lambda x:x*x*x
print(cube(10))
print()
even=lambda x:"Even" if x%2==0 else "Odd"
print(even(39))

num=[1,2,3,4,5,6,7,8]
result=list(map(lambda x:x*2, nums))
print(result)

price=[100,200,300]
final_price=list(map()  )











