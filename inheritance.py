# #single-level inheritance
# class College:
#     def college_name(self):
#         print("Maja College of Engineering")
        
# class Student(College):
#     def student_info(self):
#         print("Student Name: Karan Gandal")
#         print("Branch: Computer Science")

# obj = Student()
# obj.college_name()
# obj.student_info()

#-------------------------------------------------------------------------------

# #multi-level inheritance
# class College:
#     def college_name(self):
#         print("Maja College of Engineering")
        
# class Student(College):
#     def student_info(self):
#         print("Student Name: Karan Gandal")
#         print("Branch: Computer Science")
        
# class Exam(Student):
#     def exam_info(self):
#         print("subject1 : mathematics")
#         print("subject2 : physics")
        
# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.exam_info()

#-------------------------------------------------------------------------------

# #multiple inheritance
# class SubjMarks: # class-1  
#   Math = int(input("Enter paper marks of math :"))  
#   DE = int(input("Enter paper marks of design engineering :"))  
#   C = int(input("Enter paper marks of c language :"))  
#   English = int(input("Enter paper marks of English :"))  
# #================================= parent class -1  
# class PractMarks: # class-   
#   CPract = int(input("Enter practicals marks of c language :"))    
# #================================= parent class -2  
# class Result(SubjMarks,PractMarks): # child class  
#   #print("if student pass in both = subject and practical paper then pass")  
#   def total(self):  
#     if self.Math>=40 and self.DE>=40 and self.C>=40 and self.English>=40 and self.CPract>=20:  
#       print("pass")  
#     else:  
#       print("fail")  
# obj = Result()  
# obj.total()