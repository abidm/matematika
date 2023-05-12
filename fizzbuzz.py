import math
a = 1
b = 100

def fizzbuzz(x):
    if x % 3 == 0:
        print ("fizz")
    if x % 5 == 0:
        print ("buzz")
    if x % 3 == 0 & x % 5 == 0:
        print ("fizzbuzz")
    else:
        return True

for i in range(a, b+1):
    if fizzbuzz(i):
        print (i)
