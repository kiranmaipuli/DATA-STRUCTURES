""" finding left and right view in a binary search tree """

# inputArray = [50,30,20,40,70,60,80,10,59]
inputArray = [50,30,70,40,60,80,59]
levelDict = {}

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    # inserting nodes in a binary search tree
    def insertBinaryTree(self,node,key):
        if node != None:
            if node.value > key.value:
                if node.left == None:
                    node.left = key
                else:
                    self.insertBinaryTree(node.left,key)
                    
            elif node.value < key.value:
                if node.right == None:
                    node.right = key
                else:
                    self.insertBinaryTree(node.right,key)                                
            else:
                print("duplicates not allowed")
    
    def inOrderTraversal(self,node):
        if node == None:
            return
        self.inOrderTraversal(node.left)
        print(node.value)
        self.inOrderTraversal(node.right)

    def leftViewOfBinaryTree(self,node,level):
        if node == None:
            return
        if level not in levelDict:
            levelDict[level] = 0
            print(node.value,"left")
        self.leftViewOfBinaryTree(node.left,level + 1)
        self.leftViewOfBinaryTree(node.right,level + 1)
    
    def rightViewOfBinaryTree(self,node,level):
        if node == None:
            return
        if level not in levelDict:
            levelDict[level] = 0
            print(node.value,"right")
        self.rightViewOfBinaryTree(node.right,level + 1)
        self.rightViewOfBinaryTree(node.left,level + 1)
        
root = p = Node(inputArray[0])

for i in range(1,len(inputArray)):
    node = Node(inputArray[i])
    root.insertBinaryTree(root,node)
    
#root.inOrderTraversal(root)    
#root.leftViewOfBinaryTree(root,1)
#levelDict = {}
#root.rightViewOfBinaryTree(root,1)
########################################################################################
# right view of binary tree using breadth first search (level order traversal)

def rightViewWithBFS():
    queue = [p]
    queue1 = []
    queueLeft = []
    queueRight = []
    
    while len(queue) != 0:
        queueRight.append(queue[-1].value)
        queueLeft.append(queue[0].value)
        for i in queue:
            if i.left != None:
                queue1.append(i.left)
            if i.right != None:
                queue1.append(i.right) 
        queue = queue1
        queue1 = []
    print("right view of the binary search tree",queueRight)
    print("left view of the binary search tree",queueLeft)

rightViewWithBFS()
