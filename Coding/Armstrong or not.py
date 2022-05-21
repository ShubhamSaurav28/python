x=int(input()) #Armstrong or not
i=0
c=0
y=x
b=len(str(x))
while(i<=b):
    a=x%10
    x=x//10
    c=c+a**b
    i=i+1
if(y==c):
    print("Yes")
else:
    print("No")