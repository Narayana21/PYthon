import math
n= int(input('Enter a number: '))
f=[]
for i in str(n):
    f.append(math.factorial(int(i)))
if(sum(f)==n):
    print('Strong')
else:
    print('Not strong')