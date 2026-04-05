# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# try:
#     print("The result of division is: ", n1/n2)
# except:
#     print("can't divide by zero")
# print("to be continued...")

#----------------------------------------------------------------------------------------------

# try:
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     print("The result of division is: ", n1/n2)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("enter only integer values:")
# print("to be continued...")

#----------------------------------------------------------------------------------------------

# try: 
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)

#----------------------------------------------------------------------------------------------
# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number:", message)
# except:
#     print("this is a default part of except block")

#----------------------------------------------------------------------------------------------

# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number:", message)
# else:
#     print("Everything is ok")

#----------------------------------------------------------------------------------------------

# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number:", message)
# finally:
#     print("i will always execute")
    
#----------------------------------------------------------------------------------------------

# #nested try block
# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     try:
#         print(a/b)
#     except ZeroDivisionError as message:
#         print(message)
# except ValueError as message:
#     print(message)

#----------------------------------------------------------------------------------------------

# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)
# else:
#     print("There are no error in try block")
# finally:
#     print("i will always execute")