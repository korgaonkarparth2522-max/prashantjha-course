#wap to menu driven code
import sys
def add():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    print("Addition of a and b is:", a+b)
    
def sub():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    print("Subtraction of a and b is:", a-b)
    
def mul():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    print("Multiplication of a and b is:", a*b)
    
def div():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    print("Division of a and b is:", a/b)
    
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        print("Exiting the program...")
        sys.exit()