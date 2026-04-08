# #data structures are diiferent ways of organizing data in a computer memory that can be used effectively.
# import sys
# class Stack:
#     def __init__(self):
#         self.stacklist=[]

#     def push(self,value):
#         self.stacklist.append(value)

#     def displaystack(self):
#          print(self.stacklist)
         
#     def isEmpty(self):
#         if self.stacklist == []:
#             return True 
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist.pop()
        
#     def deleteStack(self):
#         self.stacklist = []
#         return "stack is deleted"
    
#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist[-1]
        
# stackobj = Stack()

# while True:
#     print("1.Push Element in Stack")
#     print("2.Display stack elements")
#     print("3.IS stack empty or not")
#     print("4.Pop the element from stack")
#     print("5.Delete the stack")
#     print("6.Peek a element")
#     print("7.Exit")

#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         val=int(input("Enter the value for stack: "))
#         stackobj.push(val)
#     elif choice==2:
#         stackobj.displaystack()          
#     elif choice==3:
#         print(stackobj.isEmpty())   
#     elif choice==4:
#         print(stackobj.pop())
#     elif choice==5:
#         print(stackobj.deleteStack())
#     elif choice==6:
#         print(stackobj.peek())
#     elif choice==7:
#         print("exit from the program")
        
#-----------------------------------------------------------------------------------------------

# #data structures are different ways of organizing data in computer memory
# class Stack:
#     def __init__(self):
#         self.stacklist = []

#     def push(self, value):
#         self.stacklist.append(value)

#     def displaystack(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("\nStack (Top to Bottom):")
#             print("Top")
#             for i in reversed(self.stacklist):
#                 print("-----")
#                 print(f"| {i} |")
#             print("-----")

#     def isEmpty(self):
#         return self.stacklist == []

#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stacklist.pop()

#     def deleteStack(self):
#         self.stacklist = None
#         return "Stack is deleted"

#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stacklist[-1]

# stackobj = Stack()

# while True:
#     print("\n1. Push Element in Stack")
#     print("2. Display Stack (Vertical)")
#     print("3. Check if Stack is Empty")
#     print("4. Pop Element from Stack")
#     print("5. Delete Stack")
#     print("6. Peek Element")
#     print("7. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         val = int(input("Enter the value for stack: "))
#         stackobj.push(val)

#     elif choice == 2:
#         stackobj.displaystack()

#     elif choice == 3:
#         print(stackobj.isEmpty())

#     elif choice == 4:
#         print(stackobj.pop())

#     elif choice == 5:
#         print(stackobj.deleteStack())

#     elif choice == 6:
#         print(stackobj.peek())

#     elif choice == 7:
#         print("Exit from the program")
#         break

#     else:
#         print("Invalid choice, try again!")

#-----------------------------------------------------------------------------------------------

# #data structures are diiferent ways of organizing data in a computer memory that can be used effectively.
# import sys
# class Stack:
#     def __init__(self,stacksize):
#         self.stacklist=[]
#         self.stacksize=stacksize
#     def isFull(self):
#         if len(self.stacklist)==self.stacksize:
#             return True
#         else:
#             return False    
#     def push(self,value):
#         if self.isFull():
#             print("Stack is Full")
#         else:    
#             self.stacklist.append(value)
#     def displaystack(self):
#         print("------====-----====-----=====-----====-----")
#         print(self.stacklist)
#         print("------====-----====-----=====-----====-----")
#         print()
#     def isEmpty(self):
#         if self.stacklist==[]:
#             return True
#         else:
#             return False
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist.pop()        
#     def deletestack(self):
#         self.stacklist=[] 
#         return "Stack is deleted" 
#     def peekstack(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist[-1]  

# size=int(input("Enter the size of stack: "))            
# stackobj=Stack(size)

# while True:
#     print("1.Push")
#     print("2.Display Stack element")
#     print("3.Check is empty")
#     print("4.Pop")
#     print("5.Delete stack")
#     print("6.Peek")
#     print("7.Exit")
#     print()
    
#     choice =int(input("Enter your choice:"))
#     print()
#     if choice == 1:
#         val=int(input("Enter value for stack:"))
#         stackobj.push(val)
        
#     elif choice==2:
#         stackobj.displaystack()    
        
#     elif choice==3:
#         print(stackobj.isEmpty())   
#         print() 
        
#     elif choice==4:
#         print("Poped element is:",stackobj.pop())   
#         print() 
        
#     elif choice==5:
#         stackobj.deletestack()  
        
#     elif choice==6:
#         print("The peek element is:",stackobj.peekstack()) 
#         print()   
        
#     elif choice==7:
#         sys.exit()    
#     else:
#         print("Enter Right Choice")    
#         print()