class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def insertafterval(self,data,val):
        curr=self.head
        while curr and curr.data!=val:
            curr=curr.next
        new=node(data)
        new.next=curr.next
        curr.next.prev=new
        curr.next=new
        new.prev=curr
    def delatbeg(self):
        self.head=self.head.next
        self.head.prev=None
    def delatend(self):
        self.tail=self.tail.prev
        self.tail.next=None
    def delafterval(self,val):
        curr=self.head
        while curr.data!=val:
            curr=curr.next
        curr.next=curr.next.next
        curr.next.prev=curr
    def reversedll(self):
        curr=self.head
        while curr:
            curr.next,curr.prev=curr.prev,curr.next
            curr=curr.prev
        self.head,self.tail=self.tail,self.head
    def printing(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
l1=dll()
for i in range(1,6):
    l1.insertatend(i)
l1.printing()
print()
l1.reversedll()
l1.printing()