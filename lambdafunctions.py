#Lambda functions
def s(n):
    s=n*n
    return s
print("Square of a number:",s(4))

s=lambda n:n*n
print("Square=",s(5))

a=lambda b,c:b+c
print("Additon:",a(10,30))

a=lambda x, y: x if x > y else y
print("biggest two number:", a(10, 20))

#x=int(input("Enter first number:"))
#y=int(input("Enter second number:"))
#z=lambda x,y: x if x>y else y
#print("Biggest second number:",z(x,y))

def iseven(x):
    if x%2==0:
        return True
    else:
        return False
li=[1,2,3,4,5,6,7,8,9]
data=filter(iseven,li)
print(list(data))

li=[1,2,3,4,5,6,7,8,9]
data=list(filter(lambda x:x%2==0,li))
print(data)

li = ['t','u','t','o','r','i','a','l']
data = list(filter(lambda x: x != 't', li))
print(data)
li = [20,40,60,80]
li2 = [20,30,50,20]

data = list(filter(lambda x: x not in li2, li))
print(data)




