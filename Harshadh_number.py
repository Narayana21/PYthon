n=int(input('Enter a number: '))
d=str(n)
s=0
for i in d:
    s+=int(i)
    print(i)
print(s)
if(n%s==0):
    print('success')
else:
    print('change number and try again')