"f=open('avin.txt','r')
f1=open('a.txt','w+')
str=f.read().split()
print(str)
for i in range(len(str)):
    if i%2==0:
       print(str[i])
       f1.write(str[i])
       f1.write(' ')
f1.seek(0,0)
a=f1.read()
print(a)
f1.close()
f.close()
