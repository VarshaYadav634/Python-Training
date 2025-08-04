# Single inheritance- one parent, one child 
 
class A:
    def method1(self):
        pass
    def method2(self):
        pass
class B(A):
    def method3(self):
        pass
    def method4(self):
        pass
a=A() # a.method1, a.method2
b=B() # b.method1, b.method2, b.method3, b.method4
 
 