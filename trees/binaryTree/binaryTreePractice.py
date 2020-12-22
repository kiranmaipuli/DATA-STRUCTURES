#Binary class 
inputArray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#inputArray = [1,2,3,4,5,6,7]
flag = [0]
targetDepth = [0]

class Node:
    
    # node structure of the binary tree
    def __init__(self,value):
        self.value = value
        self.leftNode = None        
        self.rightNode = None
        
    # inserting data into binary tree
    def insert(self,node,newNodeObject):
        if node.leftNode == None:
            node.leftNode = newNodeObject
            return 
        elif node.rightNode == None:
            node.rightNode = newNodeObject
            return
        else:
            sizeMatrix = self.sizeOfLeftNRightSubTrees(node)    
            height = self.heightOfTree(node,0)
            height = height - 1
            maxNoOfNodes = (2 ** height) - 1
            if (sizeMatrix[0] == sizeMatrix[1]) or (sizeMatrix[0] < maxNoOfNodes):
                self.insert(node.leftNode,newNodeObject)
            else:
                self.insert(node.rightNode,newNodeObject)
    
    # finding the size of the binary tree
    def sizeOfTree(self,node,size):
        if node != None:
            size += 1
            size = self.sizeOfTree(node.leftNode,size)
            size = self.sizeOfTree(node.rightNode,size)
        return size
    
    # size of left sub tree and rigght sub tree
    def sizeOfLeftNRightSubTrees(self,node):
        if node.leftNode == None:
            leftTreeSize = 0
        else:
            leftTreeSize = self.sizeOfTree(node.leftNode,0)
            
        if node.rightNode == None:
            rightTreeNode = 0
        else:
            rightTreeNode = self.sizeOfTree(node.rightNode,0)
        return leftTreeSize,rightTreeNode
    
    # preordertraversal using recursion
    def preOrderTraversal(self,node):
        if node != None:
            print(node.value)
            self.preOrderTraversal(node.leftNode)
            self.preOrderTraversal(node.rightNode)
                
    # finding height of the binary tree
    def heightOfTree(self,node,count):
        if node == None:
            return count
        count += 1                        
        return max(self.heightOfTree(node.leftNode,count),self.heightOfTree(node.rightNode,count))
    
    # finding the depth of the given node in the binary tree
    def findDepth(self,node,count,target):
        if node != None and flag[0] == 0:
            if node == target:
                 flag[0] == 1
                 targetDepth[0] = count
                 return
            count += 1
            self.findDepth(node.leftNode,count,target)
            self.findDepth(node.rightNode,count,target)            
              
    #inorder traversal using recursion
    def inOrderTraversal(self,node):
        if node != None:
            self.inOrderTraversal(node.leftNode)
            print(node.value)
            self.inOrderTraversal(node.rightNode)    
                
    # post order traversal using recursion            
    def postOrderTraversal(self,node):
        if node != None:
            self.postOrderTraversal(node.leftNode)
            self.postOrderTraversal(node.rightNode)                    
            print(node.value)
            
    # finding the sum of the given sub tree from the given parent node        
    def findingTheSum(self,node,target,answerString,answer):
        if node == None:
            return answer         
        if answer == "":
            target = target - node.value
            answerString = answerString + str(node.value) + ","                         
            if target == 0:
                flag[0] = 1
                answer = answerString
                return answer
            answer = self.findingTheSum(node.left,target,answerString,answer)
            answer = self.findingTheSum(node.right,target,answerString,answer)
        return answer

# inserting the nodes into the binary tree by calling recursive insert function    
root = Node(inputArray[0])        
for i in range(1,len(inputArray)):
    node = Node(inputArray[i])
    root.insert(root,node)


###################################################
# inserting nodes into binary tree using loop

def insertInBTUsingLoops():
    queue = []
    queue.append(root)
    
    for i in range(1,len(inputArray)):
        q = Node(inputArray[i])
        queue.append(q)
        if queue[0].leftNode == None:
            queue[0].leftNode = q
        elif queue[0].rightNode == None:
            queue[0].rightNode = q
            del queue[0]
            

##################################################
# breadth first traversal using loops

def bfsInBT():
    p = root
    queue = [p]
    
    while len(queue) > 0:
        print(queue[0].value)
        if queue[0].leftNode != None:
            queue.append(queue[0].leftNode)
        if queue[0].rightNode != None:
            queue.append(queue[0].rightNode)
        del queue[0]


###############################################################    
#pre order traversal in binary tree using loops

queue = [root]

def preOrderUsingLoops():
    p = root
    i = 0
    forward = 1
    backward = 0
    print(root.value)
    while len(queue) != 0:
        if backward == 1:
            if queue[i].rightNode == None:
                del queue[i]
                i = i - 1
            else:
                temp = queue[i].rightNode
                del queue[i]
                print(temp.value)
                queue.append(temp)
                forward = 1
                backward = 0
        elif queue[i].leftNode != None:
            print(queue[i].leftNode.value)
            queue.append(queue[i].leftNode)
            i = i + 1
        elif queue[i].leftNode == None: 
            forward = 0
            backward = 1
            if queue[i].rightNode == None:
                del queue[i]
                i = i - 1
                        
########################################################
#in order traversal in binary tree using loops

queue = [root]

def inOrderUsingLoops():
    p = root
    i = 0
    forward = 1
    backward = 0
    
    while len(queue) != 0:
        if backward == 1:
            if queue[i].rightNode == None:
                print(queue[i].value)
                del queue[i]
                i = i - 1
            else:
                temp = queue[i].rightNode
                print(queue[i].value)
                del queue[i]
                queue.append(temp)
                forward = 1
                backward = 0
        elif queue[i].leftNode != None:
            queue.append(queue[i].leftNode)
            i = i + 1
        elif queue[i].leftNode == None: 
            forward = 0
            backward = 1
            if queue[i].rightNode == None:
                print(queue[i].value)
                del queue[i]
                i = i - 1

    
################################################################        
# post order traversal using single stack with iteration

queue = [root]

def postOrderUsingLoops():
    p = root
    i = 0
    forward = 1
    backward = 0            
    
    while len(queue) != 0:
        if backward == 1:
            if queue[i].rightNode != None:
                queue.append(queue[i].rightNode)
                i = i + 1
                backward = 0
                forward = 1
            else:
                temp = queue[i]
                print(queue[i].value)
                del queue[i]
                i = i - 1
                while (len(queue) > 0 and queue[i].rightNode == temp):
                    print(queue[i].value)
                    temp = queue[i]
                    del queue[i]
                    i = i - 1
        elif queue[i].leftNode != None:
            queue.append(queue[i].leftNode)
            i = i + 1 
        elif queue[i].leftNode == None:
            backward = 1
            forward = 0

    
############################################################
        
# pre order traversal using one stack, easy manner

queue = [root]
            
def preOrderEasyWay():            
    p = root
    i = 0
    
    if queue[0] != None:    
        while len(queue) != 0:
            if queue[i].leftNode != None and queue[i].leftNode != None:
                queue.append(queue[i].leftNode)
                queue.append(queue[i].rightNode)
                print(queue[i].value)
                del queue[i]
                i = len(queue) - 2
            else:
                if queue[i].leftNode != None:
                    queue.append(queue[i].leftNode)
                if queue[i].rightNode != None:
                    queue.append(queue[i].rightNode)
                print(queue[i].value)
                del queue[i]
                i = len(queue) - 1
                

            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
