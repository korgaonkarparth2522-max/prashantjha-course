import sys
class Queue:
    
    def __init__(self,queueSize):
        self.queuelist=[]
        self.queueSize=queueSize
        
    def isFull(self):
        if len(self.queuelist) == self.queueSize:
            return True
        else:
            return False    
        
    def Enqueue(self,value):             #add element from rear
        if self.isFull():
            print("Queue is Full")
        else:    
            self.queuelist.append(value)
            
    def displayQueue(self):
        print("-------------------------------------------")
        print(self.queuelist)
        print("-------------------------------------------")
        print()
        
    def isEmpty(self):
        if self.queuelist == []:
            return True
        else:
            return False
        
    def Dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queuelist.pop(0) 
               
    def deleteQueue(self):
        self.queuelist = [] 
        return "Queue is Deleted" 
    
    def peek(self):                           #it returns first element of queue
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queuelist[0]  
        
size = int(input("Enter the size of queue: "))            
queueobj = Queue(size)

while True:
    print("1.Enqueue element in queue: ")
    print("2.Display queue element: ")
    print("3.Check queue is empty: ")
    print("4.Dequeue element from queue: ")
    print("5.Delete queue: ")
    print("6.Peek Operation: ")
    print("7.Exit")
    
    choice =int(input("Enter your choice:"))
    print()
    if choice == 1:
        val=int(input("Enter value for queue:"))
        queueobj.Enqueue(val)
        
    elif choice==2:
        queueobj.displayQueue()    
        
    elif choice==3:
        print(queueobj.isEmpty())   
        print() 
        
    elif choice==4:
        print(queueobj.Dequeue())   
        print() 
        
    elif choice==5:
        queueobj.deleteQueue()  
        
    elif choice==6:
        print(queueobj.peek()) 
        print()   
        
    elif choice==7:
        sys.exit()    
    else:
        print("Enter Right Choice")    
        print()