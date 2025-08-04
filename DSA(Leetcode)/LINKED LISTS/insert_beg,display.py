class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertatbeg(head,data):
    if head==None:
        head=node(data)
    else:
        new=node(data)
        new.next=head
        head=new
    return head
def printing(head):
    curr=head
    while curr:
        print(curr.data,end="->")
        curr=curr.next
head=None
for i in range(1,6):
    head=insertatbeg(head,i)
printing(head)