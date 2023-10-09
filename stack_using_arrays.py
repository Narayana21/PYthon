# # class stack:
# #     def __init__(self):
# #         self.l=[]
# #     def push(self,x):
# #         return self.l.append(x)
# #     def POP(self):
# #         if len(self.l)==0:
# #             return 'stack is Empty'
# #         return self.l.pop()
# #     def display(self):
# #         return self.l
# # q=stack()
# # i=1
# # while(i==1):
# #     print("1.Insert element to stack")
# #     print("2.Delete element to stack")
# #     print("3.Display all the element in stack")
# #     print("4.Quit")
# #     c=int(input(("Enter your choice :")))
# #     if c==1:
# #         x=int(input("insert the element in stack : "))
# #         q.push(x)
# #     elif c==2:
# #         print("Element deleted from queue is : ",q.POP())
# #     elif c==3:
# #         print('Elements ins stack',q.display())
# #     else:
# #         i=0
# class stack:
#     def __init__(self):
#         self.l=[]
#
#     def push(self,x):
#         return self.l.append(x)
#
#     def POP(self):
#         if (len(self.l)==0):
#             return 'stack is empty'
#         return self.l.pop()
#
#     def show(self):
#         return self.l
#
#
# s=stack()
# i=1
# while (i==1):
#     print('1.Insert')
#     print('2.Delete')
#     print('3.Display')
#     print('4.Exit')
#     ch=int(input('Enter your choice: '))
#     if (ch==1):
#         x=int(input('Insert the element into the stack: '))
#         s.push(x)
#     elif (ch==2):
#         print('The element deleted from stack is: ',s.POP())
#     elif (ch==3):
#         print('The elements in the stack are: ',s.show())
#     else:
#         i=0
#
#
#
#
#
#
#
#
#
#
#
#
a=str(input('Enter string: '))
b=a[::-1]
print(b.swapcase())