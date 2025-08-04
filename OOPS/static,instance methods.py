# class student:
#     def fun(): #static method
#         print("this is a method")
#     def funi(self):#this is instance method
#         print("abcdef")
# s1=student()
# student.fun()
# student.funi(s1)
# s1.funi()

# self ->instance method

class student:
    def fun(): #static method
        print("this is a method")
    def funi(self,name,marks):#this is instance method
        self.n=name
        self.m=marks
    def display(self): #this is instance method
        print(self.n,self.m)

s1=student()
s2=student()
student.fun()
student.funi(s1,"varsha",10)
student.funi(s2,"Ram Gopal",20)
s1.display()
s2.display()




