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
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new
    def insertafterval(self,data,val):
        curr=self.head
        while curr and curr.data!=val:
            curr=curr.next
        new=node(data)
        new.next=curr.next
        curr.next=new
    def delatbeg(self):
        self.head=self.head.next
    def delatend(self):
        curr=self.head
        while curr.next.next:
            curr=curr.next
        curr.next=None
    def delafterval(self,val):
        curr=self.head
        while curr.data!=val:
            curr=curr.next
        curr.next=curr.next.next
    def printing(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
l1=sll()
for i in range(1,6):
    l1.insertatend(i)
l1.printing()
print()
l1.delafterval(3)
l1.printing()