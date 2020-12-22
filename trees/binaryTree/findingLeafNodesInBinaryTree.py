""" Give an algorithm for finding the number of leaves in the binary tree without
using recursion """

#a = [1,2,3,4,5,6,7]
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def preOrderTravseral(self):
        if self != None:
            print(self.value)
            if self.left != None:
                self.left.preOrderTravseral()
            if self.right != None:
                self.right.preOrderTravseral()                

root = q = Node(a[0])        
queue = []
    
#using loop for inserting nodes
for i in range(1,len(a)):
    p = Node(a[i])
    if q.left == None:
        q.left = p
    else:
        q.right = p
        q = queue[0]
        del queue[0]
    queue.append(p)

################################################################
#finding Number of Nodes using level order traversal

leafNodes = 0

#-root.preOrderTravseral()    
if root != None:
    queue = [root]
    while len(queue) != 0:
        if queue[0].left == None and queue[0].right == None:
            leafNodes += 1
        else:
            if queue[0].left != None:
                queue.append(queue[0].left)
            if queue[0].right != None:
                queue.append(queue[0].right)                
        del queue[0]

print(leafNodes)        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    