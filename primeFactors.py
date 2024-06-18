n=int(input('Enter a number: '))
for num in range(1,n+1):
    if(n%num==0):
        count=0
        for i in range(1,num+1):
            if(num%i==0):
                count+=1
        if(count==2):
            print(num)
