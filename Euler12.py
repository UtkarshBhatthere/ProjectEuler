#Euler12
"""
Created on Tue May 1 14:33:58 2018

@author: Utkarsh Bhatt
"""
""" Any nth element of Triangular series is nothing but the sum of first n
    natural number. hence it can be stated as summation(n) = (n(n+1))/2
    For more than 500 divisors n and n+1 should have more than 501 divisors
    combined, including 2. Thus
"""
import math as m
counter = 0
i = 500
while counter < 502:
        tnum = (i*(i+1))/2
        print(tnum)
        for j in range(1, int(m.sqrt(tnum)+1)):
                if tnum % j is 0:
                        counter += 1
                        print(counter)
        i += 1