""" Given a binary tree, print out all its root-to-leaf paths """

#a = [1,2,3,4,5,6,7]
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def search(self,node,target,answer):
        if node == None:
            return answer
        if node.value == target:
            return node
        else:
            answer = self.search(node.left,target,answer)
            answer = self.search(node.right,target,answer)
        return answer    
    
    #print path in the binary tree using strings
    def printNodesUsingNodes(self,node,printString):
        if node == None:
            print(printString)
            return
        printString = printString + str(node.value) + ","
        self.printNodesUsingNodes(node.left,printString)
        if node.left == None and node.right == None:
            pass
        else:
            self.printNodesUsingNodes(node.right,printString)
    
    #print paths     
    def printNodesUsingStack(self,node,stack):
        if node == None:
            print(stack)
            return
        stack.append(node.value)
        self.printNodesUsingStack(node.left,stack)
        if node.left == None and node.right == None:
            pass
        else:
            self.printNodesUsingStack(node.right,stack)
        stack.pop()
#######################################
#insert nodes into binary tree
if len(a) != 0:
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

#########################################            
output1 = root.search(root,10,None)
output1.left = Node(19)
output1.left.right = Node(50)  
root.printNodesUsingNodes(root,"")        
root.printNodesUsingStack(root,[])        