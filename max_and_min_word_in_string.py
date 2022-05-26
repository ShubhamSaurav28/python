str=input().split()

lst=[]
for i in str:
    lst.append(len(i))

max=min=lst[0]
s=0
m=0
for i in range(len(lst)):
        if max<lst[i]:
            max=lst[i]
            m=i
        if min>lst[i]:
            min=lst[i]
            s=i
print(max,",",min)
print(str[m],",",str[s])
