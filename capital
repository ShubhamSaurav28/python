#Program to capitalize first letter of each word in a string
def myTitle(s):
    a=list(map(str,s.split()))
    j=0
    for i in a:
        b=list(i)
        x=ord(b[0])
        if x>=97 and x<=122:
            x=x-32
            b[0]=chr(x)
        b="".join(b)
        a[j]=b
        j+=1
    a=" ".join(a)
    print(a)
a=input("Enter a string: ")
myTitle(a)
