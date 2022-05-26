num=int(input())
str=bin(num)
str=str[2:]
print(str)
sum=0
for i in str:
    if i=='1':
        sum+=1
print(sum)
