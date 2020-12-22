""" creating binary tree using inorder and post order traversal """

#inOrder = [8,4,9,2,10,5,11,1,12,6,13,3,14,7,15]
#postOrder = [8,9,4,10,11,5,2,12,13,6,14,15,7,3,1]
inOrder = [2,1,4,3,5]
postOrder = [2,4,5,3,1]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def createBTUsingInAndPostOrder(self,index1,startInOrder,endInOrder):
        if index1 >= 0:
            node = Node(postOrder[index1])
            index1 -= 1
            position = 0
            if startInOrder < endInOrder:
                for i in range(startInOrder,endInOrder+1):
                    if node.value == inOrder[i]:
                        position = i
                        break
                node.right,index1 = self.createBTUsingInAndPostOrder(index1,position + 1,endInOrder)
                node.left,index1 = self.createBTUsingInAndPostOrder(index1,startInOrder,position - 1)
        else:
            node = None
        return node,index1
    
    def preOrderTraversal(self,node):
        if node == None:
            return
        print(node.value)
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

random = Node(2)
output = random.createBTUsingInAndPostOrder(len(postOrder) - 1,0,len(postOrder) - 1)    
