""" Give an algorithm for converting a tree to its mirror. Mirror of a tree is another
tree with left and right children of all non-leaf nodes interchanged. The trees below are
mirrors to each other """

a = [1,2,3,4,5,6,7]
#a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    # mirror function reverses the node structure of the binary tree
    def mirror(self,node):
        if node == None:
            return      
        self.mirror(node.left)
        self.mirror(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp
    
    def traversal(self,node):
        if node == None:
            return
        print(node.value)
        self.traversal(node.left)
        self.traversal(node.right)
#############################################
#insert nodes into binary tree using for loop
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
    
##############################################    
    
root.mirror(root)            
root.traversal(root)    
    