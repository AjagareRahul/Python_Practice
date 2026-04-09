n=[1,2,3,4,5,6]
for i in n:
    if i%2==0:
        print(i)

even=[x for x in n if x%2==0]
print(even)
print()
n=[1,2,3,4]
for i in n[::-1]:
    print(i)
print()
r=[1,2,3,4,5,6]
rs=[x for x in r[::-1]]
print(rs)
print()
nums=[10,5,20,8]
print(max(nums))

nums=[1,2,2,3,4,4]
print(list(set(nums)))
print()
nums=[10,20,4,45,99]
nums=list(set(nums))
nums.sort()
print(nums[-2])

print()
nums=[1,2,2,3,3,3]
freq={}
for i in nums:
    freq[i]=freq.get(i,0)+1

print(freq)


nums=[0,1,0,3,12]
j=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[j],nums[i]=nums[i],nums[j]
        j+=1
print(nums)
