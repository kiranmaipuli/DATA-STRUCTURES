""" check if a tree is a binary search tree """

a = [4,2,1,3,6,5,7]

class Node:
    def __init__(self,value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

    # inserting nodes into a binary search tree
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
    
    def isBSTUtil(self,root, prev): 
        if (root != None): 
            if (self.isBSTUtil(root.leftNode, prev) == True): 
                return False
            if prev != None:
                if (prev != None and
                    root.value <= prev.value): 
                    return False      
            prev = root 
            temp = self.isBSTUtil(root.rightNode, prev)
            return temp           
        return True

    # check if a tree is a binary tree
    def isBST(self,root): 
        prev = None
        return self.isBSTUtil(root, prev) 
    
    def preOrderTraversal(self,node):
        if node == None:
            return
        print(node.value)
        self.preOrderTraversal(node.leftNode)
        self.preOrderTraversal(node.rightNode)        
    
root = q = Node(a[0])

# inserting nodes into a binary search tree
#for i in range(1,len(inputArray)):
#    p = Node(inputArray[i])
#    root.insert(root,p)

queue = []

# inserting nodes in a binary tree format
for i in range(1,len(a)):
    p = Node(a[i])
    if q.leftNode == None:
        q.leftNode = p
    else:
        q.rightNode = p
        q = queue[0]
        del queue[0]
    queue.append(p)

answer = root.isBST(root)
print(answer)


