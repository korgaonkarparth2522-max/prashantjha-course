# class Student:
#     roll_no = 101  # data member
#     def studentData(self):  #member function/ method
#         print("Student information")
# obj = Student()  
# print(obj.roll_no)
# obj.studentData()  

#-----------------------------------------------------------------------------------

# #constructor 
# class Demo: 
#     def __init__(self):
#         print("This is constructor")
#     def msg(self):
#         print("This is method")
# obj = Demo()
# obj1 = Demo()
# obj.msg()

#-----------------------------------------------------------------------------------

# class Hod:
#     def __init__(self):
#         self.name = "prashant jha"  #2 bytes
#         self.age  = 45              #1 byte
#         self.emp_id = 101           #3 bytes
#     def info(self):
#         print("my name is:", self.name)
#         print("my age is:", self.age)
#         print("my emp_id is:", self.emp_id)
# obj = Hod()
# obj.info()

#-----------------------------------------------------------------------------------

# class Hod:
#     def __init__(self, name, age, emp_id):
#         self.name = name
#         self.age  = age
#         self.emp_id = emp_id
#     def show(self):
#         print("my name is:", self.name)
#         print("my age is:", self.age)
#         print("my emp_id is:", self.emp_id)
# obj = Hod("prashant jha", 45, 101)
# obj.show()

#-----------------------------------------------------------------------------------

# class New:
#     def __init__(self):
#         self.a = 10
        
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# obj1.a = 20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#-----------------------------------------------------------------------------------

# class Student:
#     def __init__(self):
#         self.s_name = "prashant"
#         self.s_age = 25
#         self.s_roll_no = 101

#     def getdata(self):
#         self.s_mb = 9876543210

# obj = Student()
# obj.getdata()
# obj.s_branch = "CSE"
# print(obj.__dict__)
# del obj.s_branch
# print(obj.__dict__)

#-----------------------------------------------------------------------------------

# class New:
#     a = 10
#     def __init__(self):
#         self.name = "prashant"
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# print()
# New.a = 50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#-----------------------------------------------------------------------------------