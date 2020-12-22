""" Give an algorithm for finding the sum of all elements in binary tree. """

a = [1,2,3,4,5,6,7]
#a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    # finds the sum of all elements in the binary tree        
    def sumOfTheTree(self,node,treeSum):
        if node == None:
            return treeSum
        treeSum += node.value
        treeSum = self.sumOfTheTree(node.left,treeSum)
        treeSum = self.sumOfTheTree(node.right,treeSum)
        return treeSum
    
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

#treeSum = root.sumOfTheTree(root,0)    
#print(treeSum)

def sumOfBTUsingBFS():
    totalSumOfTree = 0
    if root:
        queue = [root]
        while len(queue):
            totalSumOfTree += queue[0].value
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            del queue[0]
    return totalSumOfTree












