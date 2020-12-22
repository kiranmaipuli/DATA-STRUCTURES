""" Find kth smallest element in binary search tree """

inputArray = [4,2,1,3,6,5,7]

class Node:
    
    def __init__(self,value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.output = ["out of range"]

    # inserting nodes into a binary tree
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
        
    # finding kth smallest element
    def kthSmallestElementUtil(self,node,k):
        if node == None:
            return k
        k = self.kthSmallestElementUtil(node.leftNode,k)
        k -= 1      
        if k == 0:
            self.output[0] = node.value
            return k
        k = self.kthSmallestElementUtil(node.rightNode,k)        
        return k
    
    def kthSmallestElement(self,node,k):
        if k == 0:
            return self.output[0]
        self.kthSmallestElementUtil(node,k)
        
        return self.output[0]
    
root = Node(inputArray[0])
for i in range(1,len(inputArray)):
    p = Node(inputArray[i])
    root.insert(root,p)

#output = root.kthSmallestElement(root,5)
#print(output)

# finding the kth smallest element in a Binary search tree using Breadth first search

def kthSmallestWithBFS():
    p = root
    queue = [p]
    forward = 1
    k = 1
    
    if k == 0:
        return "value not present"
        
    else:    
        while queue:    
            if forward == 0:
              temp = queue[-1]
              if queue[-1].rightNode == None:
                  del queue[-1]
              else: 
                  del queue[-1]
                  queue.append(temp.rightNode)
                  forward = 1
              k = k - 1
            elif forward == 1 and queue[-1].leftNode != None:
                queue.append(queue[-1].leftNode)
            else:
                forward = 0
            if k == 0:
                answer = temp.value
                break
        return answer
print(kthSmallestWithBFS())    










