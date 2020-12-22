""" Give an algorithm for finding the number of full nodes in the binary tree without
using recursion. """

a = [1,2,3,4,5,6,7]
#a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#node class
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#traversal of the binary tree        
    def preOrderTraversal(self):
        if self != None:
            print(self.value)
            if self.left != None:
                self.left.preOrderTraversal()
            if self.right != None:
                self.right.preOrderTraversal()                

################################################################################
#inserting nodes into the binary tree        
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

#################################################################################
    
#finding the number of full nodes in a binary tree using level order traversal    
fullNodes = 0    
if root != None:    
    queue = [root]    
    while len(queue) != 0 :
        if queue[0].left != None and queue[0].right != None:
            fullNodes += 1
        if queue[0].left != None:
            queue.append(queue[0].right)
        if queue[0].right != None:
            queue.append(queue[0].right)        
        del queue[0]
    
print("number of full nodes in the given binary tree",fullNodes)

















