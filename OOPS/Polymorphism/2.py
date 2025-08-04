class A:
    def __init__(self):
        print("this is constructor a")
    def method1(self):
        print("this is method 1 of class a")
    
class B(A):
    def method1(self,a):
        print(a)
        #classname.methodname
        A.method1(self)
        A.__init__(self)
a=A()
b=B()
b.method1(5)