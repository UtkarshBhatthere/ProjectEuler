## Euler 3 Greatest prime factor
"""
Created on Sun Apr 29 18:45:09 2018

@author: Utkarsh Bhatt
"""
import math as m
num = 600851475143
limit = m.sqrt(num)
l = m.modf (limit)
limit = int(l[1])

def IsPrime(x):
    for z in range(2, int(m.sqrt(x))):
        if (x % z is 0):
            return False
            break
    return True
    

for i in range(2,limit):
    if( num % i is 0):
        if(IsPrime(i) is True):
            f = i
            
print(f)

