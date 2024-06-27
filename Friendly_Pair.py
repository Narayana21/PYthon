def fun(a,b):
    l1=[]
    l2=[]
    for i in range(1,a):
        if a%i==0:
            l1.append(i)
    for i in range(1,b):
        if b%i==0:
            l2.append(i)
    print(l1,l2)
    s1=sum(l1)
    s2=sum(l2)
    if(a/s1==b/s2):
        return True
    else:
        return False

if fun(6,28):
    print('Friendly Pair')
else:
    print('Not a friendly Pair')
