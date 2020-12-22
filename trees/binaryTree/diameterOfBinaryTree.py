""" The diameter of a tree is the number of nodes on the longest path between two leaves in the tree.  """

#a = [1,2,3,4,5,6,7]
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def travseral(self,node):     
       if node == None:
           return
       print(node.value)
       self.travseral(node.left)
       self.travseral(node.right)               
       
    def search(self,node,target,answer):
        if node == None:
            return answer
        if node.value == target:
            return node
        else:
            answer = self.search(node.left,target,answer)
            answer = self.search(node.right,target,answer)
        return answer

    # finding the height of the binary tree
    def height(self,node):
        if node == None:
            return 0
        return 1 + max(self.height(node.left),self.height(node.right))
    
    def diameter(self,node):
        if node == None:
            return 0
        lheight = self.height(node.left)
        rheight = self.height(node.right)
        ldiameter = self.diameter(node.left)
        rdiameter = self.diameter(node.right)
        return max(lheight+rheight+1,ldiameter,rdiameter)
            
########################################
#inserting nodes into binary tree
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
output1 = root.search(root,10,None)
output1.left = Node(19)
output1.left.right = Node(50)  


output = root.diameter(root)
print(output)
    
    
    