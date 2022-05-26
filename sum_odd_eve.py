#Sum of odd and even index elements in a list
lst=[]
even=0
odd=0
    
a=int(input("Enter the length of list: "))
for i in range(0,a):
    lst.append(int(input()))
for i in range(0,a,2):
    even=even+lst[i]
print("sum of even index elements: ",even)
for i in range(1,a,2):
    odd=odd+lst[i]
print("Sum of odd index elements:",odd)