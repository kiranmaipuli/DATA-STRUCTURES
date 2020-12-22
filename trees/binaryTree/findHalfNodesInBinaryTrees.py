""" Give an algorithm for finding the number of half nodes (nodes with only one
child) in the binary tree without using recursion. """

a = [1,2,3,4,5,6,7]
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    #pre-order traversal in binary tree        
    def preOrderTraversal(self):
        if self != None:
            print(self.value)
            if self.left != None:
                self.left.preOrderTraversal()
            if self.right != None:
                self.right.preOrderTraversal()                
                
    #searching an element in the binary tree                
    def search(self,target,answer):
        if self != None:
            if self.value == target:
                return self
            else:
                if self.left != None:
                    answer = self.left.search(target,answer)
                if self.right != None:
                    answer = self.right.search(target,answer)
            return answer       

#################################################
            
#inserting nodes into binary tree
root = q = Node(a[0])                
queue = []
for i in range(1,len(a)):
    p = Node(a[i])
    if q.left == None:
        q.left = p
    else:
        q.right = p
        q = queue[0]   
        del queue[0]   
    queue.append(p)
    
###################################################
    
output1 = root.search(10,None)  
output1.left = Node(19)
output1.left.right = Node(50)  


#finding half nodes in a binary tree using breadth first traversal
halfNodes = 0    
if root != None:
    queue = [root]
    while len(queue) != 0:
        if queue[0].left != None and queue[0].right == None:
            queue.append(queue[0].left)
            halfNodes += 1
        elif queue[0].left == None and queue[0].right != None:
            queue.append(queue[0].right)
            halfNodes += 1
        elif queue[0].left != None and queue[0].right != None:
            queue.append(queue[0].left)
            queue.append(queue[0].right)
        del queue[0]
print(halfNodes)        

    
    
    
    
    
    
    
    
    
    
    


