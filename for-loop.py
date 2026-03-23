'''n=int(input("Enter number:"))
for i in range(1,11):
    print(f"{n}*{i}=",n*i)

name="Rajeev"
for i in name:
    print(i)

# Control statement
for i in range(10):
    if i==5:
        break
    print(i)

for i in range(5):
    if i==2:
        continue
    print(i)

for i in range(1,51):
    print(i)


for i in range(2,51,2):
    print(i)'''
count=0
for i in range(1,30):
    if i%3==0:
        count+=1
print(count)
total=0
for i in range(1,11):
    total+=i
print(total)

