#define a function to check whether the string is pangram or not.
def isPangram(s):
    l=list(s)
    x=set(l)
    if len(x)==26:
        print("It is Pangram")
    else:
        print("It is not Pangram")

st=input("Enter a string: ")
isPangram(st)
