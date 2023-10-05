n=int(input('Enter no of elements:'))
a=[]
for i in range(0,n):
    b=int(input('enter elements: '))
    a.append(b)
avg=sum(a)/n
print('average is: ',round(avg,2))