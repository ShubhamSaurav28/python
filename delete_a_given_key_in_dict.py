d={}
x=int(input())
for i  in range (x):
    k=int(input())
    v=int(input())
    d.update({k:v})
print(d)
key=int(input())
for i in d.keys():
    if i==key:
        d.pop(i)
        break
print(d)
