from itertools import permutations as p
n=int(input('Enter a any number: '))
s=str(n)
l = list(p(s))
for i in l:
    print(''.join(i))