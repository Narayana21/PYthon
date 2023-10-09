op=0
s=''
def revv(s1,kl):
    global op
    global s
    s=s+s1[kl]
    print(s)
    if op<kl:
        revv(s1,op-1)
    else:
        pass





jk="eceasec"
revv(jk,len(jk)-1)