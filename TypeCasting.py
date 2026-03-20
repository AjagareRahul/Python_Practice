# What is type Casting?
# Converting one data type into another
# Example
#"10"-->10
#10-->"10"
#why the type casting is needed
# Because Python treat different types differently
a="10"
b="20"
print(a+b)
#1020 (string join, not addition)
print(int(a)+int(b))
#output: 30
a=1000
print(type(str(a)))
print(type(a))
print(type(float(a)))
a="Rahul"
# print(int(a)) Can not convert text to number

#Input + Type Casting
age=int(input("Enter your age:"))
#without casting input = string
# with casting input = integer
a="15"
b="5"
print(a+b)
x=10
y=3
print(x/y)
print(int(x/y))
a=5
b=2
print(float(a+b))
print(float(a)+b)

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hello"))















