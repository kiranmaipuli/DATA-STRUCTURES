""" finding maximum and minimum values in a binary tree """

inputArray = [50,30,20,40,70,60,80,10]

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

    # inserting elements in a binary tree
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
        
    def search(self,node,target,answer):
        if node == None or answer != None:
            return answer
        if node.value == target:
            answer = node
        elif target < node.value:
            answer = self.search(node.leftNode,target,answer)
        else:
            answer = self.search(node.rightNode,target,answer)
        return answer
    
    # finding minimum element in a binary search tree
    def minElement(self,node,answer):
        if node.leftNode == None:
            answer = node            
        else:
            answer = self.minElement(node.leftNode,answer)
        return answer
    
    # finding maximum element in a binary search tree
    def maxElement(self,node,answer):
        if node.rightNode == None:
            answer = node            
        else:
            answer = self.maxElement(node.rightNode,answer)
        return answer
        
        
root = Node(inputArray[0])

# inserting elements in a binary search tree
for i in range(1,len(inputArray)):
    p = Node(inputArray[i])
    root.insert(root,p)


























