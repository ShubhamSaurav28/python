def fib():
    num=int(input('enter the range:'))
    sum=0
    a,b=0,1
    print(a)
    print(b)
    for i in range(2,num):
        sum=a+b
        print(sum )
        a=b
        b=sum
fib()
