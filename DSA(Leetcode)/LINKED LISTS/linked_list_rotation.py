''' Consider a singly linked list and k value
rotate the list
 
ip-> 1->2->3->4->5
3
op-> 4->5->1->2->3 '''

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new
    def rotatesll(self,k):
        temp=self.head
        count=1
        while temp.next:
            temp=temp.next
            count+=1
        if(k>=count):
            return
        curr=self.head
        prev=None
        for i in range(k):
            prev=curr
            curr=curr.next
        prev.next=None
        temp.next=self.head
        self.head=curr
    def printing(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
o=sll()
for i in range(1,6):
    o.insertatend(i)
o.printing()
print()
o.rotatesll(5)
o.printing()

