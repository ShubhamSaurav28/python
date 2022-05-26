num=100
while num<=999:
    n=num
    sum=0
    while n>0:
        a=n%10
        n=n//10
        sum=sum+a**3
    if sum==num:
        print(num)
    num=num+1