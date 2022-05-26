str=input()
str1=""
for  i in str:
    if i not in str1:
        str1=str1+"".join(i)
print(str1)
