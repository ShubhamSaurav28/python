num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if(num1>num2):
    if(num1>num3):
        print("greatest:%d"%num1)
    else:
        print("greatest:%d"%num3)
else:
    if(num2>num3):
        print("greatest:%d"%num2)
    else:
        print("greatest:%d"%num3)
