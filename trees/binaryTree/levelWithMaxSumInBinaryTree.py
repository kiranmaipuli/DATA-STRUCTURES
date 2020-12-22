""" find the level with the maximum sum """

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def MaximumSum(self,node,count):        
        maximumSum = 0
        if node != None:
            count += 1
            if node.left != None:
                self.MaximumSum(node.left,count)
                maximumSum += node.left.value
            if node.right != None:
                self.MaximumSum(node.right,count)
                maximumSum += node.right.value                
            if count+1 not in sumOfNodesInEachLevel:
                sumOfNodesInEachLevel[count+1] = maximumSum
            else:
                sumOfNodesInEachLevel[count+1] += maximumSum                    
        
##########################################
#inserting the values into the binary tree
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

############################################
if root != None:
    sumOfNodesInEachLevel = {1:root.value}       
    root.MaximumSum(root,0)   


listOfSums = sumOfNodesInEachLevel.values()
maximumSums = max(listOfSums)


# level with maximum sum using breadth first traversal

def maxSumBFS():    
    if root != None:
        queue1 = [root]
        maximumValue = root.value
        while len(queue1) != 0:
            tempSum = 0
            queue2 = []
            for i in queue1:
                if i.left != None:
                   tempSum += i.left.value
                   queue2.append(i.left)
                if i.right != None:
                   tempSum += i.right.value
                   queue2.append(i.right)
            if tempSum > maximumValue:
                maximumValue = tempSum
            queue1 = queue2
    return maximumValue













