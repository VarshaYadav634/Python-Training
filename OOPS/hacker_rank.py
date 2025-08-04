'''
write a python program to create a class that represents a shape.
Include methods to calculate its area and perimeter. implement
subclasses for different shapes like circle, triangle and square,
'''
import math
class circle:
    def __init__(self,radius):
        self.r=radius
    def perimeter(self):
        return 2*math.pi*self.r
    def area(self):
        return math.pi*self.r*self.r
class triangle:
    def __init__(self,side1,side2,side3):
        self.s1=side1
        self.s2=side2
        self.s3=side3
        self.s=self.s1+self.s2+self.s3
    def perimeter(self):
        return self.s
    def area(self):
        return math.sqrt(self.s*(self.s-self.s1)*(self.s-self.s2)*(self.s-self.s3))
class square:
    def __init__(self,side):
        self.side=side
    def perimeter(self):
        return 4*self.side
    def area(self):
        return self.side*self.side
print("Circle- radius=3")
c=circle(3)
print("area: ",c.area())
print("perimeter: ",c.perimeter())
print("Triangle- sides = 2/3/4")
t=triangle(2,3,4)
print("area: ",t.area())
print("perimeter: ",t.perimeter())
print("Square- side=5")
s=square(5)
print("area: ",s.area())
print("perimeter: ",s.perimeter())