f=open('sample.txt','r')
n=int(input())
str=f.readlines()
for i in range(n):
    print(str[i])
f.close()
