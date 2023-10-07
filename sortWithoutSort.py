a='Narayana'
s=''
for i in range(len(a)):
    try:
        p=s[i]
        p2=s[i+1]
        if(p>p2):
            s=s+p2
    except:
        pass
print(s)

