""" binary tree """

#elements to be inserted
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#a = [1,2,3,4,5,6,7]
maximumValue = -99999999999

#using while loop
class Node:
    def __init__(self,value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        
    def preOrderTraversal(self):
        if self != None:
            print(self.value)
            if self.leftNode != None:
                self.leftNode.preOrderTraversal()            
            if self.rightNode != None:
                self.rightNode.preOrderTraversal()            
                
    def inOrderTraversal(self):
        if self != None:
            if self.leftNode != None:
                self.leftNode.inOrderTraversal()            
            print(self.value)            
            if self.rightNode != None:
                self.rightNode.inOrderTraversal()                            
                
    def postOrderTraversal(self):
        if self != None:
            if self.leftNode != None:
                self.leftNode.postOrderTraversal()
            if self.rightNode != None:
                self.rightNode.postOrderTraversal()                            
            print(self.value)
            
    # find the maximum value in a binary tree            
    def maximumValueFunction(self,maximumValue):
        if self != None:
            if maximumValue < self.value:
                maximumValue = self.value
            if self.leftNode != None:
                maximumValue = self.leftNode.maximumValueFunction(maximumValue)
            if self.rightNode != None:
                maximumValue = self.rightNode.maximumValueFunction(maximumValue)                            
        return maximumValue
    
    # find the target in the tree
    def searchTarget(self,target,answer):
        if self != None:
            if self.value == target:
                answer = True
            else:
                if self.leftNode != None and answer != True:
                    answer = self.leftNode.searchTarget(target,answer)
                if self.rightNode != None and answer != True:
                    answer = self.rightNode.searchTarget(target,answer)                                            
        return answer
    
    def findingLength(self,size):
        if self != None:
            size += 1
            if self.leftNode != None:
                size = self.leftNode.findingLength(size)
            if self.rightNode != None:
                size = self.rightNode.findingLength(size)                                            
        return size



########################################################
root = q = Node(a[0])


def printingQueue(queue):
    for i in queue:
        print(i.value,"values")


# inserting nodes into the binary tree using loops
def insertNodesInBT():        
    #for storing Nodes
    queue = []
    q = root
    #using loop for inserting nodes
    for i in range(1,len(a)):
        p = Node(a[i])
        if q.leftNode == None:
            q.leftNode = p
        else:
            q.rightNode = p
            q = queue[0]
            del queue[0]
        queue.append(p)
        
#insertNodesInBT()        
##########################################################

queue = []

#inserting nodes using recursion
def insertingNode(index,a,q,queue):
    if index < len(a):
        p = Node(a[index])
        if q.leftNode == None:
            q.leftNode = p
        else:
            q.rightNode = p
            if len(queue) > 0:
                q = queue[0]
                del queue[0]
        queue.append(p)
        insertingNode(index + 1,a,q,queue)
    else:
        return 
    
insertingNode(1,a,q,queue)    
##########################################################
#preorder traversal using stack(without recursion)

stack = [root]

def goingToRightNode(p):
    del stack[-1]
    if len(stack) != 0:
        p = stack[-1].rightNode
        del stack[-1]
        stack.append(p)
    else:
        p = "empty"
    return p

def preOrderUsingStack():
    p = root
    while stack is not None:
        if p != None:
            print(p.value)
            q = p
            p = p.leftNode
            
            # appending left node to the stack
            if p != None:
                stack.append(p)
            else:       
                
                # if leaf node is reached, then go to the right node
                if q.rightNode == None:
                    p = goingToRightNode(p)
                    if p == "empty":
                        break
                else:
                    p = p.rightNode
                    del stack[-1]
                    stack.append(p)
        elif p == None:
            p = goingToRightNode(p)
            if p == "empty":
                break


#####################################################
#in order traversal using for loop

def inOrderUsingStack():
    p = root
    stack = [p]
    
    while len(stack) != 0:
        if p != None:
            q = p
            p = p.leftNode
            if p == None:
                print(q.value)            
                del stack[-1]
                if len(stack) != 0:
                    p = stack[-1].rightNode
                    print(stack[-1].value)
                    del stack[-1]
                else:
                    break
            stack.append(p)

######################################################
#level order traversal 

def appendToQueue(p):
    if p != None:
        print(p.value)
        queue.append(p)

queue = [root]

def levelOrderTraversal():
    p = root 
    print(p.value)
    while len(queue) != 0:
        if queue[0] != None:
            appendToQueue(queue[0].leftNode)
            appendToQueue(queue[0].rightNode)
        del queue[0]            


########################################################
    






















