n=int(input('enter a number: '))
s=str(n**2)
if s.endswith(str(n)):
    print('Automorphic number')
else:
    print('not an automorphic number')
