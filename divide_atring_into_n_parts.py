str=input()
n=int(input())
m=len(str)//n
for i in range(len(str)):
    if i==m:
        print(" ",end="")
        print(str[i],end="")
        m=m+m
    else:
        print(str[i],end="")  
