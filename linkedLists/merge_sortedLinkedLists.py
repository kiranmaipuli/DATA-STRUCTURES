""" merge two sorted linked lists """
a1 = [1,7,9,10,15,19,20,21]
a2 = [2,5,8,11,17,22]

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

head1 = Node(a1[0])
head2 = Node(a2[0])

def creatingLinkedLists(linkedList,array):
    q = linkedList
    for i in range(1,len(array)):
        p = Node(array[i])
        q.next = p
        q = p
        p = p.next
        
        
creatingLinkedLists(head1,a1)
creatingLinkedLists(head2,a2)        


mergedList = None
head3 = None
count = 0

#######################################################

def updating(mergedList,currentLinkedList,head3):
    if mergedList and currentLinkedList:
        mergedList.next = currentLinkedList
        mergedList = currentLinkedList
        currentLinkedList = currentLinkedList.next
    else:
        head3 = mergedList = currentLinkedList
        currentLinkedList = currentLinkedList.next
    return mergedList,currentLinkedList,head3

p = head1
q = head2

# loop runs till both p and q are none
while p or q:
    
    # if linked list 2 reaches the end, join linked list 1 to the end of the merged list
    if p != None and q == None:
        mergedList.next = p
        p = None
        
    # if linked list 1 reaches the end, join linked list 2 to the end of the merged list    
    elif q != None and p == None:
        mergedList.next = q
        q = None
        
    #         
    elif p.value >= q.value:
        mergedList,q,head3 = updating(mergedList,q,head3)
    elif p.value <= q.value:
        mergedList,p,head3 = updating(mergedList,p,head3)
    else:
        mergedList.next = None
    
temp = head3
while temp:
    print(temp.value)
    temp = temp.next
    
""" overall complexity 

time complexity = O(n + m)
space complexity = O(n + m)

"""    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
























