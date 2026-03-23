n=0
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:    print("Zero")

n=2
if n%2==0:
    print("Even")
else:
    print("Odd")
n=-10
if n>0:
    if n%2==0:
        print("Positive even")
    else:        print("Positive odd")
elif n<0:
    if n%2==0:
        print("Negative even")
    else:        print("Negative odd")  

else:    print("Zero")

year=2024
if year%4==0 and year%100!=0 or year%400==0:
    print("{}is leap year".format(year))
else:
    print("{}is not leap year".format(year))
    