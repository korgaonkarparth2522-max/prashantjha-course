class Student:
    @staticmethod
    def get_personal_detail(first_name, last_name):
        print("your personal detail=", first_name, last_name)
        
    @staticmethod
    def contact_detail(mobile_no, roll_no):
        print("your contact detail=", mobile_no, roll_no)
        
Student.get_personal_detail("prashant", "jha")
Student.contact_detail(9876543210, 101)
Student.get_personal_detail("parth", "sharma")