# #Private class
# class Base:
#     def __init__(self):
#         print("parent class constructor called")
#         self.a = "prashant"                          #public data member
#         self.__c = "ashish"                          #private member
        
# class Derived(Base):
#     def __init__(self):
#             Base.__init__(self)
            
#             #calling constructor from Base class
#             # print("calling private member of base class: ")
#             # print(self.a)
#             # print(self.__c)
            
# obj1 = Derived()
# print(obj1.a)
# print(obj1.__c)

# obj2 = Base()
# print(obj2.a)
# print(obj2.__c)

# # private(.__) data can be only be acessible inside its class only 

#-------------------------------------------------------------------------------

# class Rbi:
#     def publicPolicy(self):
#         print("check the public policy of RBI")
        
#     def privatePolicy(self):
#         print("there is some private property which is not accessible for public")
        
# class Sbi(Rbi):
#     def _init_(self):     #first sbi class const called
#         Rbi._init_(self)  #second parent class const called
    
#     def callingPublicMethod(self):   #child class public method
#         print("\nInside child class public method")
#         self.publicPolicy()          #calling parent class public method
        
#     def callingPrivateMethod(self):  #child class public method
#         self.__privatePolicy()       #calling parent class private method will give error
        
# # obj1 = Sbi()
# # obj1.callingPublicMethod()
# # obj1.callingPrivateMethod()          #calling private method will give error
# # obj1.publicPolicy()                  #calling parent class public method
# # obj1.__privatePolicy()               #calling parent class private method will give error
# # obj2 = Rbi()
# # obj2.publicPolicy()                  #calling parent class public method
# # obj2.__privatePolicy()               #calling parent class private method will give error
# # obj2 = Rbi()
# # obj2.publicPolicy()                  #calling parent class public method
# # obj2._Rbi_privatePolicy()            #calling parent class private method using name mangling