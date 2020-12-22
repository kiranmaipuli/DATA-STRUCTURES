""" creating binary tree from in order and pre order traversal """

inOrder = [8,4,9,2,10,5,11,1,12,6,13,3,14,7,15]
preOrder = [1,2,4,8,9,5,10,11,3,6,12,13,7,14,15]
#inOrder = [2,1,4,3,5]
#preOrder = [1,2,3,4,5]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#my Binary tree
    def createBTUsingInAndPreOrder(self,node,index1,index2):
        if index2 < len(preOrder):
            if node.value != inOrder[index1]:
                node.left = Node(preOrder[index2])
                index2 += 1
                index1,index2 = self.createBTUsingInAndPreOrder(node.left,index1,index2)
                node.right = Node(preOrder[index2])
                if node.right.value == inOrder[index1]:
                    index1 += 2
                    index2 += 1
                else:
                    index2 += 1
                    index1,index2 = self.createBTUsingInAndPreOrder(node.right,index1,index2)
            else:
                index1 += 2
        return index1,index2

#textBook
    def createBTUsingInAndPreOrder1(self,index1,startInOrder,endInOrder):
        if index1 < len(preOrder):
            node = Node(preOrder[index1])
            index1 += 1
            position = 0
            if startInOrder <= endInOrder:
                for i in range(startInOrder,endInOrder+1):
                    if node.value == inOrder[i]:
                        position = i
                        break
                node.left,index1 = self.createBTUsingInAndPreOrder1(index1,startInOrder,position - 1)
                node.right,index1 = self.createBTUsingInAndPreOrder1(index1,position + 1,endInOrder)
        else:
            node = None
        return node,index1    
                    
        
    def preOrderTraversal(self,node):
        if node == None:
            return
        print(node.value)
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)
        
root = Node(preOrder[0])    
root.createBTUsingInAndPreOrder(root,0,1)
random = Node(1)
output = random.createBTUsingInAndPreOrder1(0,0,len(inOrder)-1)
