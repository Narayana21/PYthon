def seed_no(num, ref_no):
    # start writing your code here
    mul=1
    temp=num
    while temp > 0:
        rem = temp % 10
        mul= mul*rem
        temp=temp//10
    c=mul*num
    if c==ref_no:
        return True
    else:
        return False



num = 123
ref_no = 738
print(seed_no(num, ref_no))