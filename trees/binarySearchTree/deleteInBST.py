""" deleting a node from the binary tree """

a = [6,2,8,1,4,3,5,7,10]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self,node,key):
        if node != None:
            if node.value > key.value:
                if node.left == None:
                    node.left = key
                else:
                    self.insert(node.left,key)
            elif node.value < key.value:
                if node.right == None:
                    node.right = key
                else:
                    self.insert(node.right,key)                    
            else:
                print("duplicate keys are not allowed in the binary search trees")

    def delete(self,node,key):
        if node == None:
            return node
        
        if node.value == key:
            
            # if node to be deleted is the leaf node
            if node.left == None and node.right == None:
                return None

            # if node to be deleted has left child                        
            elif node.left != None and node.right == None:
                return node.left

            # if node to be deleted has right child            
            elif node.left == None and node.right != None:
                return node.right 
            
            else:
                self.insert(node.right,node.left)
                return node.right
        node.left = self.delete(node.left,key)
        node.right = self.delete(node.right,key)
        return node
                
    def preOrderTraversal(self,node):
        if node == None:
            return
        print(node.value)
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

root = Node(a[0])

for i in range(1,len(a)):
    node = Node(a[i])
    root.insert(root,node)

answer = root.delete(root,6)    
root.preOrderTraversal(answer)    