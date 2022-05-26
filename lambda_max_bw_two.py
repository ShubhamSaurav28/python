#find max between two using lambda function.
max_num=lambda a,b:a>b
a=int(input())
b=int(input())
if max_num(a,b):
    print(a)
else:
    print(b)
