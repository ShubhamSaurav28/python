def neon(num):
    sum=0
    num**=2
    while num>0:
        rem=num%10
        sum+=rem
        num//=10
    return sum
num=int(input('enter the number'))
temp=num
result=neon(num)
if result==temp:
    print('neon')
else:
    print('not neon')
