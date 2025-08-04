class A:
    def __init__(self):
        print("this is constructor a")
    def method1(self):
        print("this is method 1 of class a")
    
class B(A):
    def __init__(self):
        print("this is constructor b")
    def method1(self,a):
        print(a)
        #classname.methodname
        super().__init__()
        super().method1()
a=A()
b=B()
b.method1(5)