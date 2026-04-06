# #polymorphism
# class Principal:
#     def role(self):
#         print("I am managing all activities of the college")
        
# class Dean:
#     def role(self):
#         print("Dean = I am decision taking person of the college")
        
# class HOD:
#     def role(self):
#         print("HOD = I am managing the department of the college")
        
# class Faculty:
#     def role(self):
#         print("Faculty = I am teaching the students of the college")
        
# def func(obj):
#     obj.role()
    
# campus = [Principal(), Dean(), HOD(), Faculty()]
# for obj in campus:
#     func(obj)

#-----------------------------------------------------------------------------------------

# class arithmatic:
#     def add(self,a): 
#         print(a)
#     def add(self,a,b):
#         print(a+b) 
#     def add(self,a,b,c): 
#         print(a+b+c)

# obj=arithmatic()
# obj.add(10)        
# obj.add(10,20)        
# obj.add(10,20,30)

#-----------------------------------------------------------------------------------------

# class Arithmatic:
#     def add(self, a = None, b = None, c = None):
#         if a!= None and b != None:
#             print(a+b)
#         elif a!= None and b != None and c != None:
#             print(a+b+c)
#         else:
#             print("enter atleast 2 values")

# obj = Arithmatic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

#-----------------------------------------------------------------------------------------

# class Arithmatic:
#     def __init__(self):
#         print("there is no argument")
#     def __init__(self,a):
#         print("there is one argument")
#     def __init__(self,a,b):
#         print("there are two arguments")
        
# obj = Arithmatic()
# obj = Arithmatic(10)
# obj = Arithmatic(2,2)

#-----------------------------------------------------------------------------------------

# #overriding 
# class Rbi:
#     def home_loan(self):
#         print("home_loan = 7.5%")
#     def car_loan(self):
#         print("car_loan = 8.5%")
        
# class SBI(Rbi):
#     def home_loan(self):
#         print("home_loan = 6.5%")
#     def car_loan(self):
#         print("car_loan = 7.5%")
#         super().home_loan()
        
# obj = SBI()
# obj.home_loan()
# obj.car_loan()

#------------------------------------------------------------------------------------------

# #constructor overriding
# class Father:  
#     def __init__(self):  
#         print("Father:= i am on time at breakfast table")  
  
# class Child(Father):  
#     def __init__(self):  
#         print("Child:= i will be late for breakfast")  
          
# obj = Child()