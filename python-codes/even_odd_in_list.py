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
print('total even numbers: ',even_count)
print('They are: ',E)
print('total odd numbers: ',odd_count)
print('They are: ',O)