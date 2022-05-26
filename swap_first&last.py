#swap first and last digit of a number.
n=int(input('Enter a number: '))
first=n//(10**(len(str(n))-1))
last=n%10
x=n//10
sum=first
while x>10:
    a=x%10
    x=x//10
    sum=sum*10+a
sum=sum*10+last
p=sum
num=0
while p>0:
    q=p%10
    p=p//10
    num=num*10+q
print(num) 
    