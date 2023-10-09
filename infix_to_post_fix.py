s=['+','-','/','*','(',')']
p={'+':1,'-':1,'*':2,'/':2}

def infixtopostfix(data):
    stack=[]
    op=''
    for i in data:
        if i not in s:
            op=op+i
        elif(i=='('):
            stack.append('(')
        elif(i==')'):
            while stack and stack[-1]!='(':
                op+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and p[i]<=p[stack[-1]]:
                op+=stack.pop()
            stack.append(i)
    while stack:
        op+=stack.pop()
    return op
data='A+B-(G*B/C)'
print(infixtopostfix(data))
