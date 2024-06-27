import math
n=int(input('Enter a number: '))
sq=int(math.sqrt(n))
if((sq*sq)==n):
    print('Perfect Square')
else:
    print('Not perfect square')