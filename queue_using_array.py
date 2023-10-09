# class Queue:
#     def __init__(self):
#         self.l=[]
#     def enque(self,x):
#         return self.l.append(x)
#     def dequ(self):
#         if len(self.l)<1:
#             return 'Queue is Empty'
#         return self.l.pop(0)
#     def display(self):
#         return self.l
# q=Queue()
# i=1
# while(i==1):
#     print("1.Insert element to queue")
#     print("2.Delete element to queue")
#     print("3.Display all the element in queue")
#     print("4.Quit")
#     c=int(input(("Enter your choice : ")))
#     if c==1:
#         x=int(input("insert the element in queue : "))
#         q.enque(x)
#     elif c==2:
#         print("Element deleted from queue is : ",q.dequ())
#     elif c==3:
#         print('Elements in queue',q.display())
#     else:
#         i=0

class queue:
    def __init__(self):
        self.l=[]
    def enq(self,x):
        return self.l.append(x)
    def deq(self):
        if(len(self.l)==0):
            return 'Queue is empty'
        return self.l.pop(0)
    def display(self):
        return self.l
q=queue()
i=1
while(i==1):
    print('1. To insert')
    print('2. To delelte')
    print('3. To display')
    print('4. To quit')
    c=int(input('enter your choice: '))
    if(c==1):
        x=int(input('enter the element: '))
        q.enq(x)
    elif(c==2):
        print('The deleted element is: ',q.deq())
    elif(c==3):
        print('The elements are: ',q.display())
    else:
        i=i-1