#Euler6
"""
Created on Sun Apr 29 23:33:58 2018

@author: Utkarsh Bhatt
"""
#Mathematical formula for sum of squares is Summation(((n)(n+1)(2n+1))/6)
#while that for som of first n is Summation(((n)(n+1))/2)
#Solving the above for the require question we will get (((3n^4)+(2n^3)-(3n^2)-(2n))/12)
import math as m
def calc(x):
    result = 3*(m.pow(x,4)) + 2*(m.pow(x,3)) - 3*(m.pow(x,2)) - (2*x)
    result /= 12
    return result

print(calc(100))