# child class gives preference to it's own method when polymorphism occurs

class A:
    def method1(self,a,b):
        print(a,b)
    
class B(A):
    def method1(self,a):
        print(a)
a=A()
b=B()
b.method1(5)
