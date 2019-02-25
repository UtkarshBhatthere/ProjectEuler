#Euler10
"""
Created on Mon Apr 30 18:07:53 2018

@author: Utkarsh Bhatt
"""
import math as m
def IsPrime(x):
    for i in range(2,int(m.sqrt(x))+1):
        if x % i is 0:
            return False
            break
    return True
s = int()
for j in range(2,2000000):
    if IsPrime(j) is True:
        s = s + j
  #      print(j)


print(s)