#Program to find logarithms of a number using math module.
import math
a=float(input("Enter a number: "))
x=int(input("Enter base of: "))
print(f'log of {a} with base {x} is: ',math.log(a,x))
print(f'natural log of {a} is: ',math.log1p(a))
print(f'log of {a} with base 2 is: ',math.log2(a))
print(f'log of {a} with base 10 is: ',math.log10(a))
