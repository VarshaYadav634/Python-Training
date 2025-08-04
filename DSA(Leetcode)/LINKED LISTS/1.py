class node:
    def __init__(self,data):
        self.data=data
        self.next=None
o1=node(1)
o1.next=node(2)
o1.next.next=node(3)
print(o1,o1.data,o1.next)
print(o1.next,o1.next.data,o1.next.next)
print(o1.next.next,o1.next.next.data,o1.next.next.next)