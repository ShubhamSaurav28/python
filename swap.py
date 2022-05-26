#Input Two lists, swap first element for 1st list with last element of 2nd list and vice-verse
lst1=[]
lst2=[]
a=int(input("Length of list 1st: "))
b=int(input("Length of list 2nd: "))
print("Enter elements in list1")
for i in range(0,a):
    lst1.append(int(input()))
print("Enter elements in list 2")
for i in range(0,b):
    lst2.append(int(input()))

x=lst1
y=lst2

lst1[0]=lst1[0]^lst2[b-1]
lst2[b-1]=lst1[0]^lst2[b-1]
lst1[0]=lst1[0]^lst2[b-1]

y[0]=y[0]^x[a-1]
x[a-1]=y[0]^x[a-1]
y[0]=y[0]^x[a-1]

'''def swap(m,n):
    m=m^n
    n=m^n
    m=m^n

swap(lst1[0],lst2[b-1])
swap(y[0],x[a-1])'''
print("List 1=",lst1)
print("List 2=",y)