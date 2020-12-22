""" Give an algorithm for checking the existence of path with given sum. That
means, given a sum, check whether there exists a path from root to any of the nodes. """

#a = [1,2,3,4,5,6,7]
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sumPath = [0]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def checkIfSumExists(self,node,addedSum,path,targetSum):        
        if node == None or sumPath[0] != 0  :
            return
        path = path + str(node.value) + ","                           
        addedSum += node.value
        if addedSum == targetSum:
            sumPath[0] = path     
            return
        self.checkIfSumExists(node.left,addedSum,path,targetSum)
        self.checkIfSumExists(node.right,addedSum,path,targetSum)
        
#################################################
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


root.checkIfSumExists(root,0,"",7)    
print(sumPath)