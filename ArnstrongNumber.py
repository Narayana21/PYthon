# armstrong number of n digit number
n = int(input('enter a number '))
order = len(str(n))
sum=0
temp=n
while temp>0:
    rem=temp%10
    sum+=pow(rem,order)
    temp//=10
if n == sum:
    print(n,' is an armstrong number')
else:
    print(n,'is not an armstrong number')
