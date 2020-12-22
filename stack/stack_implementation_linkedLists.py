""" linked list implementation of stack """

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    a = "stack is empty"
    def push(self,stackName,element):
        p = Node(element)
        p.next = stackName
        return p
        stackName.append(element)

#space complexity = O(n), Time complexity = O(1)        

    def pop(self,stackName):
        if stackName == None:
            print(self.a)
            return stackName
        else:
            return stackName.next
        
#Time complexity = O(1)        

    def Top(self,stackName):
        if stackName:
            print(stackName.value)
        else:
            print(self.a)
            
#Time complexity = O(1)                    
            
    def size(self,stackName):
        count = 0
        while stackName:
            count += 1
            stackName = stackName.next
        return count
    
#Time complexity = O(n)        
    
    def isEmptyStack(self,stackName):
        if stackName:
            return False
        else:
            return True
        
#Time complexity = O(1)                
        
    def isFullStack(self,stackName,n):
        length = self.size(stackName)
        if length == n:
            return "stack is full"
        else:
            return "stack is not full"
        
#Time complexity = O(n)                

head = None    
b = Stack()    

p = head
print(b.isEmptyStack(head))

while p:
    print(p.value)
    p = p.next
#head = b.pop(head)
