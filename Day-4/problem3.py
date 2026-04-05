import csv
f = open("student1.csv", "a", newline="")
a = csv.writer(f)
# a.writerow(["rollno", "name", "mobileno", "email", "total", "percentage", "result"])

rollno = int(input("Enter roll no: "))
name = input("Enter name: ")
mobileno = int(input("Enter mobile no: "))
email = input("Enter email: ")
p1 = math = int(input("enter marks of subject 1: "))
p2 = phy = int(input("enter marks of subject 2: "))
p3 = chem = int(input("enter marks of subject 3: "))

total = p1 + p2 + p3
percentage = (total/300) * 100

if p1>=40 and p2>=40 and p3>=40:
    result = "pass"
else:
    result = "fail"
a.writerow([rollno, name, mobileno, email, total, percentage, result])