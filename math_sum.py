#Program to sum of elements in a list using math module.
import math
a=input("Enter a list of numbers in space separated form: ")
l=list(map(int,a.split()))
s=math.fsum(l)
print(s)
