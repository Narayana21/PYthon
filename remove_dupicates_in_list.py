my_list = [1, 3, 1, 2,8, 4, 5, 4 ,6, 2,7]
a=my_list
print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list,list(set(a)))