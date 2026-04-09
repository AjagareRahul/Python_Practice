for i in range(5,0,-1):
    print("*"*i)

print()
row=5
for i in range(1,row+1):
    print(' '*(row-i)+'*'*(2*i-1))
row=5

for i in range(row,0,-1):
    print(' '*(row-i)+'*'*(2*i-1))


row=5
for i in range(1,row+1):
    print('*'*i+' '*(2*(row-i))+'*'*i)
row=5
for i in range(row,0,-1):
    print('*'*i+' '*(2*(row-i))+'*'*i)

row=5
for i in range(row):
    if i==0 or i==row-1:
        print('*'*row)
    else:
        print('*'+' '*(row-2)+'*')

row=5
for i in range(row):
    if i==0 or i==row-1:
        print('*'*row)
    else:
        print('*'+' '*(row-2)+'*')

row=5
for i in range(1,row+1):
    print(' '*(row-i)+'*'+''*(2-i-3)+('*' if i> 1 else ''))

row = 5

# Upper part
for i in range(1, row+1):
    print(' '*(row-i) + '*' + ' '*(2*i-3) + ('*' if i > 1 else ''))

# Lower part
for i in range(row-1, 0, -1):
    print(' '*(row-i) + '*' + ' '*(2*i-3) + ('*' if i > 1 else ''))




for i in range(6,0,-1):
    print('*'*i)

for i in range(1,6):
    print(str(i)*i)

for i in range(1,6):
    for j in range(i):
        print(str(i)*i)

for i in range(1,6):
    print('*'*(row-1))
print()
row=5
for i in range(1,row+1):
    print('*'*(row-i))
row=5
for i in range(row,0,-1):
    print(' '*(row-i)+'*'*i)


row=5
for i in range(row,0,-1):
    print(''*(row-1)+'*'*i)
row=5
for i in range(1,row+1):
    print(' '*(row-i)+'*'*i)
        
row=5
for i in range(1,row+1):
    print(' '*(row-i)+'*'*i)

row=5
for i in range(1,row+1):
    print(''*(row-2)+'*'*i)


row=5
for i in range(1,row+1):
    print(' '*(row-i)+'*'*(2*i-1))


