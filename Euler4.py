#Euler4
"""
Created on Sun Apr 29 19:13:22 2018

@author: Utkarsh Bhatt
"""
def check():
   for i in  range (999,830,-1):
    for j in range (i, 830, -1):
        m = str(i*j)
        l = m[::-1]
        if(m in l):
            print(f"{i} and {j}")
            print(m)
            return "DONE"
        

            
check()
        

        