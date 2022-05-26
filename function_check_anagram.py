#define a function to check whether the string is anagram or not.
def isAnagram(s1,s2):
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    flag=True
    for i in range(len(l1)):
        if l1[0]!=l2[0]:
            flag=False
            break
    if flag==False:
        print("It is not Anagram")
    else:
        print("It is Anagram")
    
a=input("Enter a string: ")
b=input("Enter a string: ")
isAnagram(a,b)
