# f = open("myfile.txt", "w")         # "w" is the mode for writing to a file. If the file does not exist, it will be created. If it already exists, it will be overwritten.
# print("name of file: ", f.name)     # prints the name of the file
# print("file mode: ", f.mode)        # "r" is the mode for reading from a file. The file must exist, otherwise an error will occur.
# print("readable: ", f.readable())   # returns True if the file is readable, False otherwise
# print("writable: ", f.writable())   # returns True if the file is writable, False otherwise
# print("file closed: ", f.closed)    # returns True if the file is closed, False otherwise
# f.close()                           # closes the file
# print("file closed: ", f.closed)    # after closing the file, the closed attribute will return True

# # performing write operation
# f = open("myfile.txt", "a")
# f.write("Hello, this is a new line.")  
# f.close()
# print("file operation is done")

# f = open("myfile.txt", "w") 
# mylist = ["yash\n", "prashant\n", "patkar\n"]
# f.writelines(mylist)    # writes a list of strings to the file. Each string in the list will be written as a separate line in the file. If you want to add a newline character after each string, you can modify the list as follows:
# f.close()
# print("Data written to the file successfully.")

# # reading data from a file
# f = open("myfile.txt", "r")
# print(f.read())
# f.close()

# # with statement 
# with open("myfile.txt", "a") as f:
#     f.write("amit\n")
#     f.write("sachin\n")
#     f.write("rohit\n")
#     print("file closed: ", f.closed)
# print("file closed: ", f.closed)