# Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List

l=[1,-2,3,-4,-5,6,-7,8,-9]
es=0
os=0
ns=0
for i in l:
    if (i>0):
        if(i%2==0):
            es=es+i
        else:
            os=os+i
    else:
        ns=ns+i

print('even sum: ',es)
print('odd sum: ',os)
print('negative sum: ',ns)

