""" print all the elements in the given range present in a binary tree """

inputArray = [50,30,20,40,70,60,80,10,59]

class Node:
    def __init__(self,value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.output = ["out of range"]

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
    
    def inOrderTraversal(self,node):
        if node == None:
            return 
        self.inOrderTraversal(node.leftNode)
        print(node.value)
        self.inOrderTraversal(node.rightNode)
    
    # printing values between k1 and k2
    def printingElementsInRange(self,node,k1,k2):
        if node == None:
            return 
        self.printingElementsInRange(node.leftNode,k1,k2)
        if  k1 < node.value < k2:
            print(node.value)
        self.printingElementsInRange(node.rightNode,k1,k2)
    

    
root = Node(inputArray[0])
for i in range(1,len(inputArray)):
    p = Node(inputArray[i])
    root.insert(root,p)


root.printingElementsInRange(root,40,90)
