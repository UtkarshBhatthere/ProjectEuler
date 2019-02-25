#Euler7
"""
Created on Sun Apr 29 23:45:50 2018

@author: Utkarsh Bhatt
"""
import math as m


def IsOdd(x):
    for i in range(2, int(m.sqrt(x)+1)):
            if x % i is 0:
                print(f"Getting out for {x} with a divisior {i}")
                return False
                break
            else:
                return True     


counter = 0
n = 0
while True:
    for j in range(2, int(m.sqrt(n))):
        if IsOdd(j) is True:
                counter += 1
        if counter > 990:
                print(f"{counter}th  Prime number is {j}")
        if counter > 10005:
                break