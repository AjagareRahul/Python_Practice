num=1234
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print("Reversed:",rev)

def word_count(s):
    word=s.split()
    count={}
    for i in word:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
word_count("I love python")
print(count)
       
