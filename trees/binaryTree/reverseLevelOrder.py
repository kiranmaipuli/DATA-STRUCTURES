""" printing the binary tree in reverse order(from leaf nodes to root) using breadth first traversal """


#a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a = [1,2,3,4,5,6,7]

class Node:
    def __init__(self,value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

########################################################
root = q = Node(a[0])        
queue = []

##using loop for inserting nodes
for i in range(1,len(a)):
    p = Node(a[i])
    if q.leftNode == None:
        q.leftNode = p
    else:
        q.rightNode = p
        q = queue[0]
        del queue[0]
    queue.append(p)

########################################################
#for reverse 
p = root    
stack = []
queue = [p]

# inserting data into stack using bfs
while len(queue) != 0:
    stack.append(queue[0])
    if queue[0].rightNode != None:
        queue.append(queue[0].rightNode)
    if queue[0].leftNode != None:
        queue.append(queue[0].leftNode)
    del queue[0]
    

# retrieving data from the stack and printing the data
size = len(stack) - 1
while size >= 0:
    print(stack[size].value)    
    size -= 1












    
            