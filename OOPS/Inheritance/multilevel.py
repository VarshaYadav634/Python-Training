# Multilevel inheritance- Granfather father son
 
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
class C(B):
    def method5(self):
        pass
a=A() # a.method1, a.method2
b=B() # b.method1, b.method2, b.method3, b.method4
c=C() # c.method1, c.method2, c.method3, c.method4, c.method5
 
 