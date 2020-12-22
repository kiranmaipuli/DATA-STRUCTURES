""" insert an element in a sorted linked list """

a = [1,2,3,8,10,15,17,19]

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
head = Node(a[0])

# creating the linked list
for i in range(1,len(a)):
    p = Node(a[i])
    if i == 1:
        head.next = p
    else:
        q.next = p
    q = p

#######################################
#insert '9' in the sorted linked list
    
p = head
elementToBeInserted = Node(9)
while p != None:
    if elementToBeInserted.value < p.value:
        elementToBeInserted.next = p
        q.next = elementToBeInserted
        break
    q = p
    p = p.next
    
p = head
while p != None:
    print(p.value)
    p = p.next