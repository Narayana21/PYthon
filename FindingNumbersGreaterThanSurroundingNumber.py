
# Gives the count of numbers which are greater than the surrounding numbers

arr=[
    [1,2,3],
    [4,5,6],
    [7,3,9]
]
# for i in arr:
#     print('Current Index: ',arr.index(i))
#     for j in i:
#         print(j,'->',i.index(j))
#     print('_'*10)

a = []
count = 0
count1 = 0

for i in arr:
    for j in i:
        a.append(j)

for i in range(len(a)):
    if i % 2 == 0:
        if i == 0:
            if a[i] > a[i + 1] and a[i] > a[i + 3] and a[i] > a[i + 4]:
                count += 1
        elif i == 2:
            if a[i] > a[i + 2] and a[i] > a[i + 3]:
                count += 1
        elif i == 4:
            temp = a.copy()
            temp.pop(i)
            if a[i] > max(temp):
                count += 1
        elif i == 6:
            if a[i] > a[i - 3] and a[i] > a[i - 2] and a[i] > a[i + 1]:
                count += 1
        elif i == 8:
            if a[i] > a[i - 4] and a[i] > a[i - 3] and a[i] > a[i - 1]:
                count += 1
    else:
        if i == 1:
            if a[i] > a[0] and a[i] > a[i + 1] and a[i] > a[i + 2] and a[i] > a[i + 3] and a[i] > a[i + 4]:
                count1 += 1
        elif i == 3:
            if a[i] > a[0] and a[i] > a[i - 2] and a[i] > a[i + 1] and a[i] > a[i + 3] and a[i] > a[i + 4]:
                count1 += 1
        elif i == 5:
            if a[i] > a[i - 4] and a[i] > a[i - 3] and a[i] > a[i - 1] and a[i] > a[i + 2] and a[i] > a[i + 3]:
                count1 += 1
        elif i == 7:
            if a[i] > a[i - 4] and a[i] > a[i - 3] and a[i] > a[i - 2] and a[i] > a[i - 1] and a[i] > a[i+1]:
                count1 += 1

print('మనకి వచ్చిన కౌంట్ ఎంత అంటే :',count1 + count)