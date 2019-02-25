#Euler9
"""
Created on Mon Apr 30 16:30:21 2018

@author: Utkarsh Bhatt
"""

# For all the pythagorean triplets a, b, c there exists k and l such that:
# a = k(sq) - l (sq)
# b = 2kl
# c = k(sq) + l (sq)
# Adding them we get 2*k(sq) + 2*k*l = 1000
# solving we get 500 = k(k+l)
import math as m
for k in range(1,int(m.sqrt(500))):
    if  500 % k is 0:
        m = k
        l = 500/k - k

print((m*m - l*l)*(2*l*m)*(m*m + l*l))