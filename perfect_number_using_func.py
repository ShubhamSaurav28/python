def perfect(num):
    sum=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            sum+=i
    return sum
num=int(input('enter the number'))
temp=num
result=perfect(num)
if result==temp:
    print('perfect')
else:
    print('not perfect')
