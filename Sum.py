x=int(input('Enter a number: '))
sum=0
while x>0:
    a=x%10
    x=x//10
    sum=sum+a
print(sum)