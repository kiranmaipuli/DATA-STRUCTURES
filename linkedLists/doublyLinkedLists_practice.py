""" operations of a double linked lists """

a = [1,2,3,4,5,6,7,8]

class Node:
    
    # node structure of double linked lists
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

#############################
#creating linked list
head = Node(a[0])

for i in range(1,len(a)):
    p = Node(a[i])
    if i == 1:
        head.next = p
        p.previous = head
    else:
        q.next = p
        p.previous = q
    if i == len(a) - 1:
        tail = p
    q = p

##############################
#inserting new node at the beginning

another = Node(0)
another.next = head
head.previous = another
head = another

#############################
#inserting a new node at the end 

lastNode = Node(1000)
tail.next = lastNode
lastNode.previous = tail
tail = lastNode

###############################
#inserting a new node at 5rd position
p = head
count = 0
ithPosition = Node(200)
while p != None:
    count += 1
    if count == 4:
        temp1 = p.next
        p.next = ithPosition
        ithPosition.previous = p
        ithPosition.next = temp1
        p.next.next.previous = ithPosition
    p = p.next

##################################        






