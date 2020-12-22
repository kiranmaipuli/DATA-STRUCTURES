""" Suppose there are two singly linked lists both of which intersect at some point
and become a single linked list. The head or start pointers of both the lists are known, but
the intersecting node is not known. Also, the number of nodes in each of the lists before
they intersect is unknown and may be different in each list. List1 may have n nodes before
it reaches the intersection point, and List2 might have m nodes before it reaches the
intersection point where m and n may be m = n,m < n or m > n. Give an algorithm for
finding the merging point. """

a1 = [1,2,3,4,5,6]
a2 = [11,12,13,14,4,5,6]

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

#for i in range(1,len(linkedLists)):
#    p = linkedLists[i]
#    while p:
#        print(p.value)
#        p = p.next
#    print("end")
    
#############################################################    
#finding the merge point using hashmap
linkedList1Dict = {}
p = linkedList1
while p:
    linkedList1Dict[p] = 0
    p = p.next

""" runtime complexity = O(n1) ~ O(n1) or O(n2)
    space complexity = O(n1) ~ O(n1) or O(n2)
"""
p = linkedList2
while p:
    if p in linkedList1Dict:
        mergePoint = p
        break
    else:
        p = p.next        
print(mergePoint.value)    
""" runtime complexity = O(n2) ~ O(n)
    space complexity = O(1)
"""
    

""" overall complexity 
    runtime complexity complexity - O(n1) + O(n2)
    space complexity - O(n) + O(1) = O(n1) or O(n2)
"""    
    
    
    
    
    
    
    
        
