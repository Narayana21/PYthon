n=int(input('enter a number: '))
p=[]
for i in range(1,n):
    if(n%i==0):
        p.append(i)
print(p)
if(sum(p)==n):
    print('perfect number')
else:
    print('No perfect number')