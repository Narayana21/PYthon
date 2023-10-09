l=[1,2,3,4,5,6,7,8,9,10]
even_count=0
odd_count=0
E=[]
O=[]
for i in l:
    if(i%2==0):
        E.append(i)
        even_count+=1
    else:
        O.append(i)
        odd_count+=1
E.sort()
print('Largest even number: ',E[-1])
O.sort()
print('Largest odd number: ',O[-1])