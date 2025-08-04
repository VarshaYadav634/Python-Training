# class student:
#     def __init__(self,name,roll,m1,m2,m3):
#         self.n=name
#         self.r=roll
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3      
#     def calculate_average(self):
#         self.avg=self.m1+self.m2+self.m3/300
#         if self.m1>=35 and self.m2>=35 and self.m3>=35:
#             self.result="pass"
#         else:
#             self.result="fail"
#     def display_details(self):
#         print(self.n,self.r,self.m1,self.m2,self.m3,self.avg,self.result)
        
# s1=student("Ram",1,50,60,70)
# s2=student("Gopal",2,40,60,77)
# s3=student("Riya",3,60,55,90)
# s1.calculate_average()
# s2.calculate_average()
# s3.calculate_average()
# s1.display_details()
# s2.display_details()
# s3.display_details()


            # or

'''
task: build a "student report card" class
objective: use class, constructor, self, object creation to
manage and display student report card
 
task description: create a class called as student
 
the class should have:
1. constructor that accepts name, roll number, marks in 3 subjects
2. a method calculate_average() to compute average marks
3. a method display_details() to print student name, roll number,
marks in each subject, avg marks, result
'''
class student:
    def __init__(self,name,roll_no,m1,m2,m3):
        self.name=name
        self.roll_no=roll_no
        self.sub1=m1
        self.sub2=m2
        self.sub3=m3
        self.avg=0
    def calculate_avg(self):
        self.avg=(self.sub1+self.sub2+self.sub3)/3
    def display_details(self):
        result="pass" if self.avg>75 else "fail"
        print(self.name)
        print(self.roll_no)
        print("physics: ",self.sub1)
        print("chemistry: ",self.sub2)
        print("maths: ",self.sub3)
        print("average: ",self.avg)
        print(result)
s1=student("abcd",12,80,90,80)
s1.calculate_avg()
s1.display_details()