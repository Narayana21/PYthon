def func(n):
    return n>0


numbers=[-1,2,3,4,-8,-9]
m=map(lambda x:x>0,numbers)
l=(list(m))
print(m)
print(l)
print('postive numbers',l.count(True))
print('Negative numbers',l.count(False))