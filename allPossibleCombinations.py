from itertools import permutations
n=int(input('Enter a any number: '))
s=str(n)
l = list(permutations(s))
for i in l:
    print(''.join(i))