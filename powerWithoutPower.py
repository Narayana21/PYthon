# b=int(input('Enter base value : '))
# p=int(input('Enter power value : '))
# r=1
# for i in range(1,p+1):
#     r=r*b
# print(r)

b = int(input('Enter base value : '))
p = int(input('Enter power value : '))
r = 1
for i in range(1, p + 1):
    temp = 0
    for j in range(1, b + 1):
        temp += r
    r = temp
print(r)
