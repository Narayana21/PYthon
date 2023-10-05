
# simple interest
p=int(input("enter principal amount: "))
t=int(input("enter time period: "))
r=int(input("enter rate of interest: "))
simple_interest= (p*t*r)/100
print("simple interest for",p," is",simple_interest)

#compound interest
amount=p*(pow((1+r/100),t))
print(amount)
compound_interest= amount-p;
print('Compound interest for',p,' is',compound_interest)