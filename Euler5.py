#Euler5 - Incomplete
"""
Created on Sun Apr 29 20:46:43 2018

@author: Utkarsh Bhatt
"""
import math as m
m.l
z = set()
def IsFactor(x):
    if(y%x is 0):
        z.add(x);
        return True

def getFactor(x):    
    for y in range(1, x):
        for i in range(1,m.sqrt(y)):
            IsFactor(i)
        
getFactor(20)
product      