##Even Fibinnaci Sequence
sum = 0
f = 0
flast = 1
fn = 1

while(f < 4000000):
   f = fn + flast
   print ('f is {}'.format(f))
   flast = fn
   fn = f
   if(f % 2 is 0):
       sum = sum + f
   print(f'sum is {sum}')

print(f'Final sum is {sum}')