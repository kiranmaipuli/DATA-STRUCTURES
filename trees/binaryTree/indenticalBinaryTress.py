""" Given two binary trees, return true if they are structurally identical """

#a = []
b = [1,2,3,4,5,6]
a = [1,2,3,4,5,6,7]
output = [0]

class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None
        
    #pre order traversal
    def preOrderTravsersal(self,node):
        if node != None:
            print(node.value)
            if node.left != None:
                self.preOrderTravsersal(node.left)
            if node.right != None:
                self.preOrderTravsersal(node.right)

    #identical trees comparision
    def identicalTrees(self,node1,node2):                
        if (node1 and node2) and (output[0] == 0):
            if node1.value == node2.value:
                if node1.left and node2.left:
                    self.identicalTrees(node1.left,node2.left)
                elif node1.left == None and node2.left == None:
                    pass
                else:
                    output[0] = 1
                    return
                if node1.right and node2.right:
                    self.identicalTrees(node1.right,node2.right)
                elif node1.right == None and node2.right == None:
                    pass
                else:
                    output[0] = 1   
            else:                
                output[0] = 1
        else:
            return

##############################################
            
#inserting node into a binary tree
def insertingNodeInBinaryTree(inputArray):                
    rootNode = q = Node()             
    q.value = inputArray[0]
    queue = []
    for i in range(1,len(inputArray)):
        p = Node()
        p.value = inputArray[i]
        if q.left == None:
            q.left = p
        else:
            q.right = p
            q = queue[0]
            del queue[0]
        queue.append(p)
    return rootNode

################################################
    
#root.preOrderTravsersal(root)
root1 = insertingNodeInBinaryTree(a)
root2 = insertingNodeInBinaryTree(b)
root1.identicalTrees(root1,root2)

if len(output) > 0 and output[0] == 0:
    print(True)
else:
    print(False)    



