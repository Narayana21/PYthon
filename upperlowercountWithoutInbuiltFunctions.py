a='NarayanA'
upper=0
lower=0
for i in a:
    if ord(i)>=65 and ord(i)<=90:
        upper+=1
    elif ord(i)>=97 and ord(i)<=122:
        lower+=1
print('Upper case letters: ',upper)
print('Lower case Letters: ',lower)