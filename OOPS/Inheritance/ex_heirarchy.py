'''
Design a class hierarchy for the following:
 
Base class: Vehicle (with attributes like brand, model, year)
 
Subclasses: Car, Motorcycle, Truck
'''

class vehicle:
    def __init__(self,b,m,y):
        self.brand=b
        self.model=m
        self.year=y
class car(vehicle):
    def display(self):
        print(self.brand)
        print(self.model)
        print(self.year)
class motorcycle(vehicle):
    def display(self):
        print(self.brand)
        print(self.model)
        print(self.year)
class truck(vehicle):
    def display(self):
        print(self.brand)
        print(self.model)
        print(self.year)
c=car("Benz","qseries",2020)
c.display()
m=motorcycle("splender","abc",2022)
m.display()
t=truck("tata","xyz",2024)
t.display()
