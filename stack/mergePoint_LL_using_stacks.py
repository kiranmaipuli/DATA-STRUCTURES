""" finding the merge point in the merged linked list using stacks """


# defining the structure of node in a linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
 
#####################################################
#creating two singly linked lists which intersect
jointList = [4,5,6]
list1 = [1,2,3]
list2 = [11,12,13,14]
jointLinkedList = Node(jointList[0])
linkedList1 = Node(list1[0])
linkedList2 = Node(list2[0])

def createLinkedList(count,lists,linkedList):
    if count < len(lists):
        p = Node(lists[count])
        linkedList.next = p
        linkedList = p
        count += 1
        createLinkedList(count,lists,linkedList)
    else:
        if lists != jointList:
            linkedList.next = jointLinkedList 

lists = [jointList,list1,list2]
linkedLists = [jointLinkedList,linkedList1,linkedList2]

for i in range(0,len(lists)):
    createLinkedList(1,lists[i],linkedLists[i])           

############################################################
#merge point 
stack1 = []
stack2 = []

def traversingNAdding(linkedListName,stackName):    
    while linkedListName:
        print(linkedListName.value)
        stackName.append(linkedListName)
        linkedListName = linkedListName.next
traversingNAdding(linkedList1,stack1)        
traversingNAdding(linkedList2,stack2)        
temp = None

while stack1 and stack2:
    temp = stack2[-1]
    if stack1[-1] == temp:
        mergePoint = temp
        del stack1[-1]
        del stack2[-1]
    else:
        break
        
print(mergePoint.value,"merge value")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















