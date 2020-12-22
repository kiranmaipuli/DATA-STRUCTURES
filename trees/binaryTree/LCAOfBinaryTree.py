""" Give an algorithm for finding LCA (Least Common Ancestor) of two nodes in a
Binary Tree. """

#a = [1,2,3,4,5,6,7]
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
paths = []

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    # getting path of the given targets from root        
    def findPathsOfNodes(self,node,target1,target2,temp):
        if node == None:
            return
        if (node.value == target1) or (node.value == target2):
            p = temp[:]
            paths.append(p)            
        temp.append(node.value)
        self.findPathsOfNodes(node.left,target1,target2,temp)
        self.findPathsOfNodes(node.right,target1,target2,temp)
        temp.pop()
        
################################################################
#insert nodes into binary tree using for loop
        
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

root.findPathsOfNodes(root,15,10,[])

# getting the least common ancestor from the paths obtained

if len(paths) == 0:
    print("given two nodes do not exist in the tree")
elif len(paths) == 1:
    print("only one of the given two nodes exist in the tree")
else:
    a_set = set(paths[0]) 
    b_set = set(paths[1]) 
  
    if (a_set & b_set): 
        common = a_set & b_set
        print(list(common)[-1]) 
    else: 
        print("No common elements")  
