""" finding the shortest distance between two nodes in a binary search tree """

inputArray = [50,30,20,40,70,60,80,10,59]

""" Time and space complexity 
    Best case: O(1), O(1)
    Average case: O(log(n)), - balanced tree - O(h)
    Worst case: O(n) , O(n)

"""

class Node:
    def __init__(self,value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

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
    
    def preOrderTraversal(self,node):
        if node == None:
            return
        print(node.value)
        self.preOrderTraversal(node.leftNode)
        self.preOrderTraversal(node.rightNode)
    
    # finding the least common anscestor
    def LCA(self,target1,target2,node,flag,lca):
        if node == None:
            return lca
        if flag == 0:
            if node.value > target1 and node.value > target2:
                lca = self.LCA(target1,target2,node.leftNode,flag,lca)
            elif node.value < target1 and node.value < target2:
                lca = self.LCA(target1,target2,node.rightNode,flag,lca)
            else:
                flag = 1
                lca = node
        return lca
    
    # shortest distance betwenn two nodes
    def heightOfNode(self,node,heightl,heightr,flag,target):
        if node == None:
            return max(heightl,heightr),flag
        if flag == 0:
            if target < node.value:
                templ = self.heightOfNode(node.leftNode,heightl,heightr,flag,target)
                heightl = templ[0] + 1
                flag = templ[1]
            elif target > node.value:
                tempr = self.heightOfNode(node.rightNode,heightl,heightr,flag,target)
                heightr = tempr[0] + 1
                flag = tempr[1]
            else:
                flag = 1
        return max(heightl,heightr),flag
    
    
root = Node(inputArray[0])
for i in range(1,len(inputArray)):
    p = Node(inputArray[i])
    root.insert(root,p)


lca = root.LCA(59,20,root,0,None)
print(lca.value)

# height of node with value 20 from the least common ancestor
height1 = root.heightOfNode(lca,0,0,0,20)

# height of node with value 59 from the least common ancestor
height2 = root.heightOfNode(lca,0,0,0,59)

# shortest distance between two nodes is the sum of individual heights from the least common ancestor 
shortDistance = height1[0] + height2[0]
print(shortDistance)





















