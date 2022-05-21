x=int(input())
t=0
i=2
while(i<x):
    if(x%i==0):
        t=1
    i=i+1    
if(t==0):
    print("prime")
else:
    print("Not prime")