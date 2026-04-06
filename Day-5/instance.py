class Student:
    def __init__(self, name, roll_no, mob):
        self.name = name          #instance variable
        self.roll_no = roll_no    #instance variable
        self.mob = mob            #instance variable
        
    def display(self):  #instance method
        print(self.name,"",self.roll_no," ",self.mob)
        
stud = Student("prashant", 101, 9876543210)
stud.display()