""" How to design a stack such that GetMinimum( ) should be O(1) """
a = [100,2,3,-1,5,-3]
minStack = []
mainStack = []

class Stack:
    
    # inserting new element into the stack
    def push(self,element):
        mainStack.append(element)        
        
        # if the element is less than the last inserted element of min stack, then insert the new element
        if minStack:
            if mainStack[-1] <= minStack[-1]:
                minStack.append(mainStack[-1])
        else:
            minStack.append(element)
            
    # delete the last inserted element from the main stack            
    def pop(self):
        if mainStack:
            
            # while popping out the last element from the main stack, check whether that element is present in the min stack
            if mainStack[-1] == minStack[-1]:
                del minStack[-1]
            del mainStack[-1]            
            
    # display the last inserted element from the main stack            
    def Top(self):
        if mainStack:
            print(mainStack[-1])
    
    # display the minimum element of the main stack                        
    def minimum(self):
        if minStack:
            print(minStack[-1])

# initiating stack object
b = Stack()        
for i in a:
    b.push(i)






             