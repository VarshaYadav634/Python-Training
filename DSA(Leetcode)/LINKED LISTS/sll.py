class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
l1=sll()
for i in range(1,6):
    l1.insertatbeg(i)
l1.printing()