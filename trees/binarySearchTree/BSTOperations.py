""" binary search tree operations """

inputArray = [50,30,20,40,70,60,80,10,59]

""" Time and space complexity 
    Best case: O(1), O(1)
    Average case: O(log(n)), - balanced tree - O(h)
    Worst case: O(n) , O(n)

"""

class Node:
    def __init__(self,value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

    # inserting nodes into the binary tree
    def insert(self,node,element):
        if node != None:
            if element.value < node.value:
                if node.leftNode == None:
                   node.leftNode = element         
                   return 
                else:
                    self.insert(node.leftNode,element)
            elif element.value > node.value:
                if node.rightNode == None:
                   node.rightNode = element         
                   return 
                else:
                    self.insert(node.rightNode,element)
            else:
                print("duplicates are not allowed")
    
    def preOrderTraversal(self,node):
        if node == None:
            return
        print(node.value)
        self.preOrderTraversal(node.leftNode)
        self.preOrderTraversal(node.rightNode)
            
    # finding minimum value in the binary search tree
    def minElement(self,node,answer):
        if node.leftNode == None:
            answer = node            
        else:
            answer = self.minElement(node.leftNode,answer)
        return answer
    
    # finding maximum value in the binary search tree
    def maxElement(self,node,answer,targetParent):
        if node == None:
            return answer,targetParent
        if node.rightNode == None:
            answer = node                        
        elif answer == None:
            answer,targetParent = self.maxElement(node.rightNode,answer,node)
        return answer,targetParent
        
        
root = Node(inputArray[0])
for i in range(1,len(inputArray)):
    p = Node(inputArray[i])
    root.insert(root,p)
























