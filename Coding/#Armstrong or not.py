#Armstrong or not
i=0
x=0
while(i<=1000):
    x=i
    c=0
    while(x>0):
        a=x%10
        x=x//10
        c=c+a**len(str(i))
    if(c==i):
        print(i)
    i=i+1
   