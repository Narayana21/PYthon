a=[25,1,2,3,4]
max=a[0]
l=[]
for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)