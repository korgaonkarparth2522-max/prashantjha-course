# #CRUD operations

# from operator import index
# import sys
# class Employee:
#     def __init__(self):
#         print("employee management system")
#         self.emp_id = []
#         self.emp_name = []
#         self.emp_city = []
#         self.emp_salary = []
        
#     def createEmployee(self):
#         self.emp_id.append(int(input("enter employee id: ")))
#         self.emp_name.append(input("enter employee name: "))
#         self.emp_city.append(input("enter employee city: "))
#         self.emp_salary.append(float(input("enter employee salary: ")))

#     def readallEmployee(self):
#         for i in range(len(self.emp_id)):
#             print(f"Employee ID: {self.emp_id[i]}")
#             print(f"Employee Name: {self.emp_name[i]}")
#             print(f"Employee City: {self.emp_city[i]}")
#             print(f"Employee Salary: {self.emp_salary[i]}")
#         else:
#             print("employee id not found")

#     def updateEmployee(self):
#         emp_id = int(input("enter employee id to update: "))
#         if emp_id in self.emp_id:
#             index = self.emp_id.index(emp_id)
#             self.emp_name[index] = input("enter new employee name: ")
#             self.emp_city[index] = input("enter new employee city: ")
#             self.emp_salary[index] = float(input("enter new employee salary: "))
#         else:
#             print("employee id not found")
            
#     def deleteEmployee(self):
#         emp_id = int(input("enter employee id to delete: "))
#         if emp_id in self.emp_id:
#             index = self.emp_id.index(emp_id)
#             del self.emp_id[index]
#             del self.emp_name[index]
#             del self.emp_city[index]
#             del self.emp_salary[index]
#         else:
#             print("employee id not found")
            
# obj = Employee()

# while True:
#     print("1. Create Employee")
#     print("2. Read All Employee")
#     print("3. Update Employee")
#     print("4. Delete Employee")
#     print("5. Exit")
    
#     choice = int(input("enter your choice: "))
    
#     if choice == 1:
#         obj.createEmployee()
#     elif choice == 2:
#         obj.readallEmployee()
#     elif choice == 3:
#         obj.updateEmployee()
#     elif choice == 4:
#         obj.deleteEmployee()
#     elif choice == 5:
#         print("exiting the program...")
#         sys.exit()

#--------------------------------------------------------------------------------------------

import sys

class CRUD:
    def __init__(self):
        print("Student Management System")
        self.studentId=[]
        self.studentName=[]
        self.studentRollNo=[]
        self.studentCity=[]
        
    def addStudent(self):
        self.studentId.append(input("Enter student Id :"))
        self.studentName.append(input("Enter student Name :"))
        self.studentRollNo.append(input("Enter student Roll No :"))
        self.studentCity.append(input("Enter student City :"))
        
    def ShowStudent(self):
        print("Student ID: \t\t StudentName \t\t StudentRollno \t\t City")
        print("----------------------------------------------------------------------------------")
        for i in range(len(self.studentId)):
            print(self.studentId[i],"\t\t\t",self.studentName[i],"\t\t\t",self.studentRollNo[i],"\t\t\t",self.studentCity[i])
            print("----------------------------------------------------------------------------------")
            
    def updateStudent(self):
        id=input("Enter student ID to update: ")
        if id in self.studentId:
            while True:
                    print("1. Update Student Name")
                    print("2. Update Student Roll No")
                    print("3. Update Student City")
                    print("4. Exit")
                    choice=int(input("Enter your choice: "))
                    
                    if choice==1:
                        index=self.studentId.index(id)
                        self.studentName[index]=input("Enter new student name: ")
                        print("Student name updated successfully")
                    elif choice==2:
                        index=self.studentId.index(id)
                        self.studentRollNo[index]=int(input("Enter new student roll no: "))
                        print("Student roll no updated successfully")
                    elif choice==3:
                        index=self.studentId.index(id)
                        self.studentCity[index]=input("Enter new student city: ")
                        print("Student city updated successfully")
                    elif choice==4:
                        break
                    else:
                        print("Invalid choice")
            index=self.studentId.index(id)
            self.studentName[index]=input("Enter new student name: ")
            self.studentRollNo[index]=int(input("Enter new student roll no: "))
            self.studentCity[index]=input("Enter new student city: ")
            print("Student updated successfully")
        else:
            print("Student ID not found")

    def deleteStudent(self):
        id=input("Enter student ID to delete: ")
        if id in self.studentId:
            index=self.studentId.index(id)
            del self.studentId[index]
            del self.studentName[index]
            del self.studentRollNo[index]
            del self.studentCity[index]
            print("Student deleted successfully")
        else:
            print("Student ID not found")
            
obj=CRUD()
while True:
    print("1. Add Student")
    print("2. Show Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        obj.addStudent()
    elif choice==2:
        obj.ShowStudent()
    elif choice==3:
        obj.updateStudent()
    elif choice==4:
        obj.deleteStudent()
    elif choice==5:
        sys.exit()
    else:
        print("Invalid choice")