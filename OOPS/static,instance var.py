class student:
    course='cse' # static var
    def __init__(self,x):
        self.name=x #instance var
    def fun(self,a):
        print("this is a method",a,self.name,student.course) # a= local var
    
s1=student('riya')
s2=student('abhi')
s1.fun(3)
s2.fun(5)