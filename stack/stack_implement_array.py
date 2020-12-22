""" stack implementation using lists """

a = []

class Stack:
    def push(self,stackName,element):
        stackName.append(element)
    def pop(self,stackName):
        del stackName[-1]
    def Top(self,stackName):
        return stackName[-1]
    def size(self,stackName):
        return len(stackName)
    def isEmptyStack(self,stackName):
        if stackName:
            return False
        else:
            return True
    def sFullStack(self,stackName,n):
        if len(stackName) == n:
            return "stack is full"
        else:
            return "stack is not full"
      
b = Stack()
#print(b.isEmptyStack(a))
b.push(a,5)
b.pop(a)
print(a)        