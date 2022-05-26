num=int(input("enter the number:"))
temp=num
sum=0
while(num>0):
    rem=num%10
    fact=1
    while(rem>0):
        fact=fact*rem
        rem-=1
    sum+=fact
    num=num//10
if(temp==sum):
    print("the number is a strong number!")
else:
    print("the number is not a strong number!")
