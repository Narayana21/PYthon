# l=[]
# def s(n,k):
#     global l
#     print(n-k,end=' ')
#     l.append(n-k)
#     if((n-k)<=0):
#         return
#     s(n-k,k)
# def s1(n,k,s):
#     print(n+k,end=' ')
#     if((n+k)==s):
#         return
#     s1(n+k,k,s)
# n=15
# k=5
# s(n,k)
# s1(l[-1],k,n)
op=0
r=26
m=0
def jk(i):
    global op
    global r
    global m
    if op==0:
        m=r-i
    if m<=0:
        op=1
    if op==1:
        m=r+i
    if m==r:
        pass
    else:
        jk(i)
    print(m)
jk(3)
