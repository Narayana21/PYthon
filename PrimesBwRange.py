# prime numbers between range

lower = int(input('enter lower range'))
upper = int(input('enter upper range'))
for i in range(lower,upper+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
          count=count+1
    if(count==2):
        print(i,end='  ')




